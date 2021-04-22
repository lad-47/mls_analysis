var columnDefs;
var columnDefsCurrent;
var rowData;
var rowDataCurrent;
var gridOptions;
var gridDiv;
var grid;

var west = ['MIN','SKC','COL','NSH','DAL','POR','SEA','LAFC','VAN','HOU','RSL','LA','SJ','ATX']
var east = ['TOR','ATL','CIN','NYC','RBNY','NE','MIA','DCU','CHI','CLB','MTL','PHI','ORL']

$.ajax({
	type: "GET",  
	url: "https://raw.githubusercontent.com/lad-47/mls_analysis/master/mls_analysis_calc.csv",
	dataType: "text",       
	success: function(response)  
	  {
      columnDefs = $.csv.toArrays(response).shift().map(a => {
        return {
          headerName: a,
          field: a,
          sortable: true,
          width: 100,
          resizable: true
        }
      });
      rowData = $.csv.toObjects(response);
      columnDefsCurrent = columnDefs.slice(0,5);
      columnDefsCurrent[2].sort = 'desc';
      columnDefsCurrent[3].sort = 'desc';
      columnDefsCurrent[4].sort = 'desc';

      // let the grid know which columns and what data to use
      gridOptions = {
        columnDefs: columnDefsCurrent,
        rowData: rowData,
        domLayout: 'autoHeight',
        sortingOrder: ['desc', 'asc', null],
      };

      // setup the grid after the page has finished loading
      gridDiv = document.querySelector('#myGrid');
      grid = new agGrid.Grid(gridDiv, gridOptions);
	  }   
});
document.addEventListener('input', function (event) {
	if (event.target.id === 'stats') {
    if (parseInt(event.target.value) === 1) {
      columnDefsCurrent = columnDefs.slice(0,5);
    }
    if (parseInt(event.target.value) === 2) {
      columnDefsCurrent = [columnDefs[0],...columnDefs.slice(5,9)];
    }
    if (parseInt(event.target.value) === 3) {
      columnDefsCurrent = [columnDefs[0],...columnDefs.slice(9,13)];
    }
    if (parseInt(event.target.value) === 4) {
      columnDefsCurrent = [columnDefs[0],...columnDefs.slice(13,17)];
    }
    if (parseInt(event.target.value) === 5) {
      columnDefsCurrent = [columnDefs[0],...columnDefs.slice(17,21)];
    }
    if (parseInt(event.target.value) === 6) {
      columnDefsCurrent = [columnDefs[0],...columnDefs.slice(21,25)];
    }
    if (parseInt(event.target.value) === 7) {
      columnDefsCurrent = [columnDefs[0],...columnDefs.slice(25,29)];
    }
    if (parseInt(event.target.value) === 8) {
      columnDefsCurrent = [columnDefs[0],...columnDefs.slice(29,33)];
    }
    columnDefsCurrent[2].sort = 'desc';
    columnDefsCurrent[3].sort = 'desc';
    columnDefsCurrent[4].sort = 'desc';
    if (parseInt(event.target.value) === 9) {
      columnDefsCurrent = [columnDefs[0],...columnDefs.slice(33,34)];
      columnDefsCurrent[1].sort = 'desc';
    }
    gridOptions.api.setColumnDefs(columnDefsCurrent);
  }
	if (event.target.id === 'conference') {
    if (event.target.value === 'SHIELD') {
      rowDataCurrent = rowData;
    }
    if (event.target.value === 'WEST') {
      rowDataCurrent = rowData.filter(r => west.includes(r.Team));
    }
    if (event.target.value === 'EAST') {
      rowDataCurrent = rowData.filter(r => east.includes(r.Team));
    }
    gridOptions.api.setRowData(rowDataCurrent);
  }
}, false);