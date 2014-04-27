

var ctx = document.getElementById("chart").getContext("2d");

var data = {
    labels : graph_labels,
    datasets : [
        {
            fillColor : "#4044B8",
            strokeColor : "rgba(220,220,220,1)",
            data : precision_scores
        },
        {
            fillColor : "#40B85E",
            strokeColor : "rgba(220,220,220,1)",
            data : recall_scores
        },
        {
            fillColor : "#B84042",
            strokeColor : "rgba(220,220,220,1)",
            data : f1_scores
        },
    ]
}
var options = {'scaleOverride' : true, 'scaleSteps' : 20, 'scaleStepWidth': 4, 'scaleStartValue' : 20};
var chart = new Chart(ctx).Bar(data, options);