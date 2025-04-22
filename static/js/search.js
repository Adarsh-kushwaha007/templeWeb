script.js
const items = [
    'Tamil Nadu',
    'Maharashtra',
    'Karnataka',
    'West Bengal',
    'Gujarat',
    'Tamil Nadu',
    'Maharashtra',
    'Karnataka',
    'West Bengal',
    'Gujarat',
    // Add more items as needed
];

const searchInput = document.getElementById('searchInput');
const resultsContainer = document.getElementById('results');

searchInput.addEventListener('input', handleSearch);

function handleSearch() {
    const query = searchInput.value.toLowerCase();
    const filteredItems = items.filter(item => item.toLowerCase().includes(query));

    displayResults(filteredItems);
}

function displayResults(filteredItems) {
    resultsContainer.innerHTML = '';
    filteredItems.forEach(item => {
        const cont = document.createElement('div');
        cont.textContent = item;
        resultsContainer.appendChild(cont);
    });
}


// script.js
const city = [
    'Tamil Nadu',
    'Maharashtra',
    'Karnataka',
    'West Bengal',
    'Gujarat',
    'Tamil Nadu',
    'Maharashtra',
    'Karnataka',
    'West Bengal',
    'Gujarat',
    // Add more items as needed
];

const SearchInput = document.getElementById('SearchInput');
const ResultsContainer = document.getElementById('Results');

SearchInput.addEventListener('input', handleSearchCity);

function handleSearchCity() {
    const query = SearchInput.value.toLowerCase();
    const filteredcity = city.filter(cities => cities.toLowerCase().includes(query));

    displayCityResults(filteredcity);
}

function displayCityResults(filteredcity) {
    ResultsContainer.innerHTML = '';
    filteredcity.forEach(city => {
        const citycont = document.createElement('div');
        citycont.textContent = city;
        ResultsContainer.appendChild(citycont);
    });
}


