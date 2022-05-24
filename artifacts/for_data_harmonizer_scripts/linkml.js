/** --------------------------------------------------------- */
/** Messaging interface for NMDC Portal-- Do not modify above */
/** --------------------------------------------------------- */
/** Once DOM has loaded, set up the interface */
$(document).ready(async () => {
    // this introduces the GOLD_ECOSYSTEM_TREE global variable
    await $.ajax({
        "cache": false,
        "dataType": "script",
        "crossDomain": true,
        "url": "template/nmdc_dh/GoldEcosystemTree.js",
        "method": "GET",
    });
    
    // a simple data structure to define the relationships between the GOLD ecosystem fields
    const GOLD_FIELDS = {
        ecosystem: {
            upstream: [],
            downstream: ['ecosystem_category', 'ecosystem_type', 'ecosystem_subtype', 'specific_ecosystem'],
        },
        ecosystem_category: {
            upstream: ['ecosystem'],
            downstream: ['ecosystem_type', 'ecosystem_subtype', 'specific_ecosystem'],
        },
        ecosystem_type: {
            upstream: ['ecosystem', 'ecosystem_category'],
            downstream: ['ecosystem_subtype', 'specific_ecosystem'],
        },
        ecosystem_subtype: {
            upstream: ['ecosystem', 'ecosystem_category', 'ecosystem_type'],
            downstream: ['specific_ecosystem'],
        },
        specific_ecosystem: {
            upstream: ['ecosystem', 'ecosystem_category', 'ecosystem_type', 'ecosystem_subtype'],
            downstream: [],
        },
    };
    
    function getSameRowCellData(dh, columnNames) {
        const [row, rest] = dh.hot.getSelectedLast();
        return columnNames.map(columnName => {
            const col = dh.getFields().findIndex(field => field.name === columnName);
            if (col < 0) {
                return null;
            }
            return dh.hot.getDataAtCell(row, col);
        })
    }
    
    function getGoldOptions(path = []) {
        // ideally GOLD_ECOSYSTEM_TREE wouldn't be a global variable, but we need a module system first
        if (!window.GOLD_ECOSYSTEM_TREE) {
            return []
        }
        let options = window.GOLD_ECOSYSTEM_TREE.children;
        for (let name of path) {
            const item = options.find(child => child.name === name);
            if (!item) {
                options = [];
                break;
            }
            options = item.children;
        }
        return options.map(child => child.name)
    }
    
    const fieldSettings = {}
    for (let field of Object.keys(GOLD_FIELDS)) {
        fieldSettings[field] = {
            getColumn: function (dh, col) {
                // define a dynamic source field. this function gets the 'upstream' dependent fields,
                // looks up the valid completions in the GOLD classification tree, and provides those
                // as the autocomplete options
                col.source = (_, next) => {
                    const dependentRowData = getSameRowCellData(dh, GOLD_FIELDS[field].upstream)
                    const options = getGoldOptions(dependentRowData);
                    next(options);
                };
                col.type = 'autocomplete';
                col.trimDropdown = false;
                return col;
            },
            
            onChange: function(change, fields, triggered_changes) {
                // clear downstream fields if the value changes
                if (change[2] !== change[3]) {
                    for (let other of GOLD_FIELDS[field].downstream) {
                        const otherIdx = fields.findIndex(f => f.title === other)
                        triggered_changes.push([change[0], otherIdx, change[2], null])
                    }
                }
            }
        }
    }
    
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
    dh.field_settings = fieldSettings;
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
