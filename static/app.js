const $list = $("#cupcake-list");
const $form = $("#new-cupcake-form");
const $searchForm = $("#search-form")
const cakes = []


$form.on('submit', submitCake)
$searchForm.on('submit', searchForFlavor)

loadCakes();

async function searchForFlavor(evt) {
    evt.preventDefault();

    $searchInput = $('#cupcake-search');
    const term = $searchInput.val();
    const cakes = await getCakesByFlavor(term);
    if (cakes.length) {
        refillCakeList(cakes);
        //$searchInput.val('');
    } else {
        alert('No Results...');
    }
}


async function submitCake(evt) {
    evt.preventDefault();
    const newCake = getCakeFromForm();
    const result = await createCake(newCake)
    if (result) {
        addCake(result);
        clearCakeForm();
    } else {
        alert('Something about that didn\'t work...')
    }
}



async function loadCakes() {
    const newCakes = await getAllCakes();
    cakes.push(...newCakes)
    refillCakeList(newCakes)
}

function refillCakeList(newCakes) {
    //empty the list if full
    $list.html('')
    for (let cake of newCakes) {
        addCake(cake);
    }
}


function getCakeFromForm() {
    flavor = $('#flavor').val();
    size = $('#size').val();
    image = $('#image').val();
    rating = $('#rating').val();
    return { flavor, size, image, rating };
}
function clearCakeForm() {
    $('#flavor').val('');
    $('#size').val('');
    $('#image').val('');
    $('#rating').val('');
}



function addCake(cake) {
    const html = makeCupcakeCard(cake);
    const $newCake = $(html);
    $list.append($newCake);
}


function makeCupcakeCard(cake) {
    let html = `<div class="card col-12 col-md-6 col-lg-4 col-xl-3">`;
    if (cake.image) {
        html += `<img class="card-img-top" src="${cake.image}" alt="photo of a ${cake.flavor} flavored Cupcake">`;
    } else {
        html += `<img class="card-img-top" src="" alt="No Photo Available">`;
    }
    html += `<div class="card-body">
                    <h5 class="card-title">A ${cake.size} ${cake.flavor} Cupcake!</h5>
                <p class="card-info">${cake.rating} Stars</p>
            </div>
        </div>`;
    return html;
}