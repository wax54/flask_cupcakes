const $list = $("#cupcake-list");
const $form = $("#new-cupcake-form");
const cakes = []


$form.on('submit', submitCake)

loadCakes();

async function submitCake(evt) {
    evt.preventDefault();
    const newCake = getCakeFromForm();
    result = await createCake(newCake)
    if (result) {
        addCake(result);
        clearCakeInputs();
    } else {
        alert('Something about that didn\'t work...')
    }


}

function getCakeFromForm() {
    flavor = $('#flavor').val();
    size = $('#size').val();
    image = $('#image').val();
    rating = $('#rating').val();
    return { flavor, size, image, rating };
}
function clearCakeInputs() {
    $('#flavor').val('');
    $('#size').val('');
    $('#image').val('');
    $('#rating').val('');
}


async function loadCakes() {
    const newCakes = await getAllCakes();
    for (let cake of newCakes) {
        cakes.push(cake);
        addCake(cake);
    }
}

function addCake(cake) {
    const $newCake = $(`<li id="${cake.id}" class="cupcake" >`);
    $newCake.html(cake.flavor);
    $list.append($newCake);
}

