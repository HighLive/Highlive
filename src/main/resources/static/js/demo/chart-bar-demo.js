// Set new default font family and font color to mimic Bootstrap's default styling
Chart.defaults.global.defaultFontFamily = 'Nunito', '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#858796';

function number_format(number, decimals, dec_point, thousands_sep) {
  // *     example: number_format(1234.56, 2, ',', ' ');
  // *     return: '1 234,56'
  number = (number + '').replace(',', '').replace(' ', '');
  var n = !isFinite(+number) ? 0 : +number,
    prec = !isFinite(+decimals) ? 0 : Math.abs(decimals),
    sep = (typeof thousands_sep === 'undefined') ? ',' : thousands_sep,
    dec = (typeof dec_point === 'undefined') ? '.' : dec_point,
    s = '',
    toFixedFix = function(n, prec) {
      var k = Math.pow(10, prec);
      return '' + Math.round(n * k) / k;
    };
  // Fix for IE parseFloat(0.55).toFixed(0) = 0;
  s = (prec ? toFixedFix(n, prec) : '' + Math.round(n)).split('.');
  if (s[0].length > 3) {
    s[0] = s[0].replace(/\B(?=(?:\d{3})+(?!\d))/g, sep);
  }
  if ((s[1] || '').length < prec) {
    s[1] = s[1] || '';
    s[1] += new Array(prec - s[1].length + 1).join('0');
  }
  return s.join(dec);
}

emotionChartLabels = []
emotionChartData = []

$.getJSON("http://"+ window.location.host + "/api/emotion/" + videoId, function(data) {
  $.each(data, function(key, value){
    emotionChartLabels.push(value[0]);
    emotionChartData.push(parseFloat(value[1]));
  });
});

// 페이지가 로드 된 이후 canvas 그리기
window.addEventListener('load', ()=> {
  // Bar Chart Example
  var ctx = document.getElementById("myBarChart");
  var myBarChart = new Chart(ctx, {
    type: 'bar',
    data: {
      labels: emotionChartLabels,
      datasets: [{
        data: emotionChartData,
        backgroundColor: [
          'rgba(216, 27, 96, 0.6)',
          'rgba(3, 169, 244, 0.6)',
          'rgba(255, 152, 0, 0.6)',
          'rgba(29, 233, 182, 0.6)',
          'rgba(156, 39, 176, 0.6)',
          'rgba(84, 110, 122, 0.6)'
        ],
        borderColor: [
          'rgba(216, 27, 96, 1)',
          'rgba(3, 169, 244, 1)',
          'rgba(255, 152, 0, 1)',
          'rgba(29, 233, 182, 1)',
          'rgba(156, 39, 176, 1)',
          'rgba(84, 110, 122, 1)'
        ],
        borderWidth: 1
      }]
    },
    options: {
      maintainAspectRatio: false,
      legend: {
        display: false
      },
      scales: {
        xAxes: [{
          time: {
            unit: 'emotion'
          },
          gridLines: {
            display: false,
            drawBorder: false
          },
          ticks: {
            maxTicksLimit: 6
          },
        }],
        yAxes: [{
          ticks: {
            min: 0,
            max: 100,
            maxTicksLimit: 5,
            padding: 10,
            // Include a dollar sign in the ticks
            callback: function(value, index, values) {
              return '' + number_format(value);
            }
          },
          gridLines: {
            color: "rgb(234, 236, 244)",
            zeroLineColor: "rgb(234, 236, 244)",
            drawBorder: false,
            borderDash: [2],
            zeroLineBorderDash: [2]
          }
        }],
      },
    }
  });
})
