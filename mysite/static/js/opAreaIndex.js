var opArea = "{{ opArea }}"
	var url = "http://127.0.0.1:8000/data/" + opArea + "/"
	var dataText;
	var dataArray;

	var xHR = new XMLHttpRequest();
	xHR.onload = handleStateChange;
	xHR.open("GET", url);
	xHR.send();

	function handleStateChange(){
		if( xHR.status >= 200 &&
			xHR.status < 300) {
		dataText = xHR.responseText;
		}

		dataArray = processData(dataText);
	}

	function processData(dataText) {
		dataText = String(dataText);
		var allTextLines = dataText.split(/\n/);
		var headers = allTextLines[0].split(',');
		var load = [];
		var temp = [];
		var wind = [];
		for (var i=1; i<allTextLines.length; i++) {
			var data = allTextLines[i].split(',');
			if (data.length == headers.length) {

				var loadLine = [];
				var tempLine = [];
				var windLine = [];
				for (var j=0; j<headers.length; j++) {
					if(j==0){
						var dateString = (data[0] + " " + data[1]);
						var date = new Date(dateString)
						loadLine[0] = date;
						tempLine[0] = date;
						windLine[0] = date;
					}
					if(j==2){
						loadLine[1] = (Number(data[j]));
					}
					if(j==3){
						tempLine[1] = (Number(data[j]));
					}
					if(j==4){
						windLine[1] = (Number(data[j]));
					}
					if(j==5){
						loadLine[2] = (Number(data[j]));
					}
					if(j==6){
						tempLine[2] = (Number(data[j]));
					}
					if(j==7){
						windLine[2] = (Number(data[j]));
					}
				}
				load.push(loadLine);
				temp.push(tempLine);
				wind.push(windLine);

			}
		}
		 drawGraphs(load, temp, wind);
		 updateStats(load, temp, wind);
	}

	function drawGraphs(load, temp, wind){

      new Dygraph(
          document.getElementById("load"),
          load,
          {
			labels: ["time", "actual load", "forecasted load"],
            title: 'Load for {{ opArea }}',
            ylabel: 'Load (MW)',
            legend: 'always',
            labelsDivStyles: { 'textAlign': 'center' },
            showRangeSelector: true,
			rangeSelectorHeight: 30,
          }
      );
      new Dygraph(
          document.getElementById("temp"),
          temp,
          {
			labels: ["time", "actual temperature", "forecasted temperature"],
            title: 'Temperatures for {{ opArea }}',
            ylabel: 'Temperature (F)',
            legend: 'always',
            labelsDivStyles: { 'textAlign': 'right' },
            showRangeSelector: true,
            rangeSelectorHeight: 30,
          });

	new Dygraph(
          document.getElementById("windSpeed"),
          wind,
          {
			labels: ["time", "actual wind speed", "forecasted wind speed"],
            title: 'Wind Speed for {{opArea}}',
            ylabel: 'Wind Speed (mph)',
            legend: 'always',
            labelsDivStyles: { 'textAlign': 'right' },
            showRangeSelector: true,
            rangeSelectorHeight: 30,
          });
	}

	function updateStats(load, temp, wind){
		document.getElementById("loadNumber").innerHTML = generateRandomNumber(load);
		document.getElementById("tempNumber").innerHTML = generateRandomNumber(temp);
		document.getElementById("windNumber").innerHTML = generateRandomNumber(wind);
	}

	 window.onload = generateRandomNumber;
     function generateRandomNumber(data){

         var n = 25;
         var number = Math.floor(Math.random()*n)+1;

		 var indexNum = 0;
		 var sum	= 0;
		 var count = 1;

		 i=0;
		k=0;
		for(count=0;count<data.length;count++)
		{
			var actual = data[count][1];
			var forecast = data[count][2];
			sum += (Math.abs(forecast - actual)/actual);
		}

		var answer = sum / count;

		return answer;

     }