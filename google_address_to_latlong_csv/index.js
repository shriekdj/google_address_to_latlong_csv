var arrival_date = document.getElementById("arrival_date");

var departure_date = document.getElementById("departure_date")

function updateDepartureDate() {
	departure_date.value = arrival_date.value;
	departure_date.min = arrival_date.value;
}

arrival_date.setAttribute('onchange', 'updateDepartureDate()')
