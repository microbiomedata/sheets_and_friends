/** --------------------------------------------------------- */
/** Messaging interface for NMDC Portal-- Do not modify above */
/** --------------------------------------------------------- */
/** Once DOM has loaded, set up the interface */
$(document).ready(async () => {
    async function loadScript(path) {
        return await $.ajax({
            "cache": false,
            "dataType": "script",
            "crossDomain": true,
            "url": path,
            "method": "GET",
        });
    }

    await loadScript("template/nmdc_dh/GoldEcosystemTree.js");
    await loadScript("template/nmdc_dh/ConfigureFieldSettings.js");

    /**
    * Call from the regular launch function to set up
    * additional behavior for integration for NMDC submission portal
    *
    * This method is called when a new template is launched.
    */
    DataHarmonizer.overrideGetColumnCoordinates = function () {
        const ret = {};
        let column_ptr = 0;
        for (section of this.template) {
            ret[section.title] = { '': column_ptr };
            for (column of section.children) {
                ret[section.title][column.title] = column_ptr;
                column_ptr++;
            }
        }
        return ret;
    };
    
    DataHarmonizer.updateParentState = function () {
        const columnCoordinates = this.overrideGetColumnCoordinates();
        const INVALID_CELLS = this.invalid_cells;
        window.parent.postMessage({ type: 'update', INVALID_CELLS, columnCoordinates }, "*");
    };
    
    /**
    * Handle new file upload.
    */
    DataHarmonizer.processFileChange = function (file) {
        const ext = file.name.split('.').pop();
        const acceptedExts = ['xlsx', 'xls', 'tsv', 'csv'];
        if (!acceptedExts.includes(ext)) {
            const errMsg = `Only ${acceptedExts.join(', ')} files are supported`;
            $('#open-err-msg').text(errMsg);
            $('#open-error-modal').modal('show');
        } else {
            this.invalid_cells = {};
            this.runBehindLoadingScreen(this.openFile, [this, file]);
            $('#file_name_display').text(file.name);
        }
        // Allow consecutive uploads of the same file
        $('#open-file-input')[0].value = '';
        
        $('#next-error-button,#no-error-button').hide();
        this.current_selection = [null, null, null, null];
    }
    
    const setupMessageInterface = (dh) => {
        const params = new URLSearchParams(location.search);
        if (params.get('minified') || false) {
            console.log("minified=true; Setting up DataHarmonizer message interface...");
            // Toolbar and modals share a common parent, so this is a hack to only hide the toolbar.
            $('#data-harmonizer-toolbar-inset').children().slice(0, 6).attr('style', 'display:none !important');
            
            window.addEventListener("message", async (event) => {
                switch (event.data.type) {
                    case 'setupTemplate':
                    dh.setupTemplate(event.data.folder);
                    break;
                    
                    case 'open':
                    dh.processFileChange(event.data.files);
                    break;
                    
                    case 'validate':
                    dh.validate();
                    dh.updateParentState();
                    break;
                    
                    case 'jumpToRowCol':
                    dh.scrollTo(event.data.row, event.data.column);
                    break;
                    
                    case 'changeVisibility':
                    if (['all', 'required', 'recommended'].includes(event.data.value)) {
                        dh.changeColVisibility(`show-${event.data.value}-cols-dropdown-item`);
                    } else {
                        const ptr = Object.keys(dh.overrideGetColumnCoordinates()).indexOf(event.data.value);
                        dh.changeColVisibility(`show-section-${ptr}`);
                    }
                    break;
                    
                    case 'exportJson':
                    const value = [...dh.getFlatHeaders(), ...dh.getTrimmedData()];
                    window.parent.postMessage({ type: 'exportJson', value }, "*");
                    break;
                    
                    case 'loadData':
                    while (!dh.hot) {
                        await new Promise((resolve) => window.setTimeout(resolve, 100));
                    }
                    dh.hot.loadData(event.data.data);
                    break;
                    
                    case 'showReference':
                    dh.renderReference();
                    break;
                    
                    default:
                    console.log('Unknown Type', event.data.type);
                }
            });
        }
    }
    
    /************************** APPLICATION LAUNCH ********************/
    
    let dh = new Object(DataHarmonizer);
    DataHarmonizerConfig.applyNmdcFieldSettings(dh);
    let toolbar = new Object(DataHarmonizerToolbar);
    setupMessageInterface(dh);
    
    
    const myDHGrid = document.getElementById('data-harmonizer-grid');
    const myDHToolbar = document.getElementById('data-harmonizer-toolbar');
    const myDHFooter = document.getElementById('data-harmonizer-footer');
    
    // This is just a way to move toolbar html into place as an alternative
    // to loading it dynamically from a separate html file.
    $(myDHToolbar).append($('#data-harmonizer-toolbar-inset'));
    $('#data-harmonizer-toolbar-inset').css('visibility','visible');
    
    // Note: TEMPLATES contains templates/menu.js object. It is only required
    // if using dh.getTemplate() below without specifying a template.
    await dh.init(myDHGrid, myDHFooter, TEMPLATES);
    
    await toolbar.init(dh, myDHToolbar);
    
    // Picks first template in dh menu if none given in URL.
    let template_path = dh.getTemplate();
    // Hardcode URL here if desired. Expecting a file path relative to app's template folder.
    await dh.useTemplate(template_path)
    
    await toolbar.refresh();
    
    dh.updateParentState();
});
