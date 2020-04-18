function load_chart(labels, real, average, worst, best) {

    var config = {
        type: 'line',
        data: {
            labels: labels,
            datasets: [
                {
                    label: "Reality",
                    fill: true,
                    backgroundColor: 'rgb(16,191,3)',
                    borderColor: 'rgb(71,75,71)',
                    data: real,
                    lineTension: 0,
                    pointRadius: 5,
                    pointHoverRadius: 10,
                    datalabels: {
                        color: 'rgb(16,191,3)',
                        align: 'top',
                        offset: '0'
                    }
                },
                {
                    label: "Average",
                    fill: false,
                    backgroundColor: 'rgb(16,191,3)',
                    borderColor: 'rgb(16,191,3)',
                    borderDash: [5, 5],
                    data: average,
                    lineTension: 0,
                    datalabels: {
                        color: 'rgb(16,191,3)',
                        align: 'top',
                        offset: '0'
                    }
                },
                {
                    label: "Worst",
                    fill: false,
                    backgroundColor: 'rgb(221, 13, 13)',
                    borderColor: 'rgb(221, 13, 13)',
                    borderDash: [5, 5],
                    data: worst,
                    lineTension: 0,
                    datalabels: {
                        color: 'rgb(221,13,13)',
                        align: 'bottom',
                        offset: '0'
                    }
                },
                {
                    label: "Best",
                    fill: false,
                    backgroundColor: 'rgb(10, 3, 196)',
                    borderColor: 'rgb(10, 3, 196)',
                    borderDash: [5, 5],
                    data: best,
                    lineTension: 0,
                    datalabels: {
                        color: 'rgb(10,3,196)',
                        align: 'top',
                        offset: '0'
                    }
                }]
        },
        options: {
            responsive: true,
            spanGaps: true,
            elements: {
                point: {
                    pointStyle: 'rectRot'
                }
            },
            title: {
                display: true,
                text: 'Burnup '
            },
            tooltips: {
                mode: 'index',
                intersect: false,
            },
            hover: {
                mode: 'nearest',
                intersect: true
            },
            scales: {
                xAxes: [{
                    display: true,
                    scaleLabel: {
                        display: true,
                        labelString: 'Sprint'
                    }
                }],
                yAxes: [{
                    display: true,
                    scaleLabel: {
                        display: true,
                        labelString: 'Story points'
                    }
                }]
            }
        }
    }
    var ctx = document.getElementById("canvas").getContext("2d");
    window.myLine = new Chart(ctx, config);
}