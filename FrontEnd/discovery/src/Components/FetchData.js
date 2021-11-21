//@author: AJWuu

<script async src="https://maps.googleapis.com/maps/api/js?key=YOUR_API_KEY&callback=initMap"></script>

const map = new google.maps.Map(document.getElementById("map"), {});
var list = new List();
var output = new List();

function searchClothes() {
    list.append("clothes");
}

function searchFood() {
    list.append("food");
}

function searchLeisure() {
    list.append("leisure");
}

function searchService() {
    list.append("service");
}

function searchStore() {
    list.append("gift&store");
}

function searchAll() {
    output = api.searchOutput(list);
    list = new List(); //return to empty list
}
