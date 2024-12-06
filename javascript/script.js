let select = "Pluie";

barCanvas = document.getElementById("barCanvas");

barChart = new Chart(barCanvas , {
    type: "line",
    data: {
        labels: ["0h", "3h", "6h", "9h", "12h", "15h", "18h", "21h"],
        datasets: [{
            data: value_graph_today,
            fill: true,
            backgroundColor: "cyan"
        }],
    },
    options: {
        scales: {
            y: {
                min: 0,
                max : 100,
                ticks: {
                    callback: function(value, index, values) {
                      return value + ' %';
                    }
                }
            }
        },
        plugins: { legend: { display: false } } // Enlever le bouton cacher le graphique
    }
});

// barChart.options.scales.y.max

selectButton(1);

document.getElementById('btn_today_rain').addEventListener('click', function() {
    selectButton(1);
    if(select == "Pluie") {
        barChart.data.datasets[0].data = value_graph_today;
    }
    if(select == "Vent") {
        barChart.data.datasets[0].data = value_graphSpeed_today;
        refreshMaxValueTableau(value_graphSpeed_today);
    }
    if(select == "Humidité") {
        barChart.data.datasets[0].data = value_graphHumidity_today;
    }
    barChart.update();
});

document.getElementById('btn_tomorrow').addEventListener('click', function() {
    selectButton(2);
    if(select == "Pluie") {
        barChart.data.datasets[0].data = value_graph_tomorrow;
    }
    if(select == "Vent") {
        barChart.data.datasets[0].data = value_graphSpeed_tomorrow;
        refreshMaxValueTableau(value_graphSpeed_tomorrow);
    }
    if(select == "Humidité") {
        barChart.data.datasets[0].data = value_graphHumidity_tomorrow;
    }
    barChart.update();
});

document.getElementById('btn_after_tomorrow').addEventListener('click', function() {
    selectButton(3);
    if(select == "Pluie") {
        barChart.data.datasets[0].data = value_graph_after_tomorrow;
    }
    if(select == "Vent") {
        barChart.data.datasets[0].data = value_graphSpeed_after_tomorrow;
        refreshMaxValueTableau(value_graphSpeed_after_tomorrow);
    }
    if(select == "Humidité") {
        barChart.data.datasets[0].data = value_graphHumidity_after_tomorrow;
    }
    barChart.update();
});

choiceSelectButton(1);

document.getElementById('btn-rain').addEventListener('click', function() {
    select = "Pluie";
    choiceSelectButton(1);
    selectButton(1);
    barChart.data.datasets[0].data = value_graph_today;
    barChart.options.scales.y.max = 100;
    barChart.options.scales.y.ticks.callback = function(value) {
        return value + ' %';
    };
    barChart.update();
});

document.getElementById('btn-speed').addEventListener('click', function() {
    select = "Vent";
    choiceSelectButton(2);
    selectButton(1);
    barChart.data.datasets[0].data = value_graphSpeed_today;
    refreshMaxValueTableau(value_graphSpeed_today);
    barChart.options.scales.y.ticks.callback = function(value) {
        return value + ' km/h';
    };
    barChart.update();
});

document.getElementById('btn-humidity').addEventListener('click', function() {
    select = "Humidité";
    choiceSelectButton(3);
    selectButton(1);
    barChart.data.datasets[0].data = value_graphHumidity_today;
    barChart.options.scales.y.max = 100;
    barChart.options.scales.y.ticks.callback = function(value) {
        return value + ' %';
    };
    barChart.update();
});

function refreshMaxValueTableau(tableau) {
    let max_value = 0;
    for (let i = 0; i < tableau.length; i++) {
        if (tableau[i] > max_value) {
            max_value = tableau[i];
        }
    }
    barChart.options.scales.y.max = max_value;
}

function selectButton(btn_id) {
    document.getElementById('btn_today_rain').style.backgroundColor = "#808080";
    document.getElementById('btn_today_rain').style.color = "#fff";
    document.getElementById('btn_tomorrow').style.backgroundColor = "#808080";
    document.getElementById('btn_tomorrow').style.color = "#fff";
    document.getElementById('btn_after_tomorrow').style.backgroundColor = "#808080";
    document.getElementById('btn_after_tomorrow').style.color = "#fff";

    if(btn_id==1) {
        document.getElementById('btn_today_rain').style.backgroundColor = "#469cf3";
        document.getElementById('btn_today_rain').style.color = "#000";
    }
    if(btn_id==2) {
        document.getElementById('btn_tomorrow').style.backgroundColor = "#469cf3";
        document.getElementById('btn_tomorrow').style.color = "#000";
    }
    if(btn_id==3) {
        document.getElementById('btn_after_tomorrow').style.backgroundColor = "#469cf3";
        document.getElementById('btn_after_tomorrow').style.color = "#000";
    }

}

function choiceSelectButton(btn_id) {
    document.getElementById('btn-rain').style.backgroundColor = "#808080";
    document.getElementById('btn-rain').style.color = "#fff";
    document.getElementById('btn-speed').style.backgroundColor = "#808080";
    document.getElementById('btn-speed').style.color = "#fff";
    document.getElementById('btn-humidity').style.backgroundColor = "#808080";
    document.getElementById('btn-humidity').style.color = "#fff";

    if(btn_id==1) {
        document.getElementById('btn-rain').style.backgroundColor = "#fff";
        document.getElementById('btn-rain').style.color = "#000";
    }
    if(btn_id==2) {
        document.getElementById('btn-speed').style.backgroundColor = "#fff";
        document.getElementById('btn-speed').style.color = "#000";
    }
    if(btn_id==3) {
        document.getElementById('btn-humidity').style.backgroundColor = "#fff";
        document.getElementById('btn-humidity').style.color = "#000";
    }

}

function validateSearch() {
    window.location.href = "./"+document.getElementById("input-search").value;
}

document.getElementById('btn-search').addEventListener('click', function() {
    validateSearch();
});

document.getElementById('input-search').addEventListener('keydown', function(event) {
    if (event.key === 'Enter') {
        validateSearch();
    }
});

/* Modifier lors du clique du boutton */

/*// Pluie
document.getElementById('btn-rain').addEventListener('click', function() {
    if(document.getElementById('btn-rain').textContent=="Précipitation") {
        document.getElementById('btn-rain').textContent = "Précipitation en %";

        document.getElementById('btn-speed').textContent = "Vent";
        document.getElementById('btn-humidity').textContent = "Humidité";
    } else {
        document.getElementById('btn-rain').textContent = "Précipitation";
    }
});

// Vent
document.getElementById('btn-speed').addEventListener('click', function() {
    if(document.getElementById('btn-speed').textContent=="Vent") {
        document.getElementById('btn-speed').textContent = "Vent en km/h";

        document.getElementById('btn-rain').textContent = "Précipitation";
        document.getElementById('btn-humidity').textContent = "Humidité";
    } else {
        document.getElementById('btn-speed').textContent = "Vent";
    }
});


// Humidité
document.getElementById('btn-humidity').addEventListener('click', function() {
    if(document.getElementById('btn-humidity').textContent=="Humidité") {
        document.getElementById('btn-humidity').textContent = "Humidité en %";

        document.getElementById('btn-rain').textContent = "Précipitation";
        document.getElementById('btn-speed').textContent = "Vent";
    } else {
        document.getElementById('btn-humidity').textContent = "Humidité";
    }
});*/
