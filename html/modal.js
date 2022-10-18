const openModalButton = document.getElementById('open-modal');
const modalWindowOverlay = document.getElementById('modal-overlay');
const closeModalButton = document.getElementById('close-modal');

const pizza = document.querySelectorAll("[id='cards-pizza']");
const pizza_button = document.getElementById('pizza-button');

const salad = document.querySelectorAll("[id='cards-salad']");
const salad_button = document.getElementById('salad-button');

const pasta = document.querySelectorAll("[id='cards-pasta']");
const pasta_button = document.getElementById('pasta-button');

const dessert = document.querySelectorAll("[id='cards-dessert']");
const dessert_button = document.getElementById('dessert-button');

const drinks = document.querySelectorAll("[id='cards-drinks']");
const drinks_button = document.getElementById('drinks-button');

const showModalWindow = () => {
  modalWindowOverlay.style.display = 'flex';
};

const hideModalWindow = () => {
  modalWindowOverlay.style.display = 'none';
};
const hideModalWindowOnBlur = (e) => {
  if (e.target === e.currentTarget) {
    hideModalWindow();
  }
};

pizza_button.onclick = function () {
  pizza_button.style.background = '#F2E8CF';
  salad_button.style.background = '#6a994e';
  pasta_button.style.background = '#6a994e';
  dessert_button.style.background = '#6a994e';
  drinks_button.style.background = '#6a994e';
  for (let i = 0; i < pizza.length; i++) {
    pizza[i].style.display = 'block';
    salad[i].style.display = 'none';
    pasta[i].style.display = 'none';
    dessert[i].style.display = 'none';
    drinks[i].style.display = 'none';
  }
};

salad_button.onclick = function () {
  salad_button.style.background = '#F2E8CF';
  pizza_button.style.background = '#6a994e';
  pasta_button.style.background = '#6a994e';
  dessert_button.style.background = '#6a994e';
  drinks_button.style.background = '#6a994e';
  for (let i = 0; i < salad.length; i++) {
    pizza[i].style.display = 'none';
    salad[i].style.display = 'block';
    pasta[i].style.display = 'none';
    dessert[i].style.display = 'none';
    drinks[i].style.display = 'none';
  }
};

pasta_button.onclick = function () {
  pasta_button.style.background = '#F2E8CF';
  pizza_button.style.background = '#6a994e';
  salad_button.style.background = '#6a994e';
  dessert_button.style.background = '#6a994e';
  drinks_button.style.background = '#6a994e';
  for (let i = 0; i < pasta.length; i++) {
    pizza[i].style.display = 'none';
    salad[i].style.display = 'none';
    pasta[i].style.display = 'block';
    dessert[i].style.display = 'none';
    drinks[i].style.display = 'none';
  }
};
dessert_button.onclick = function () {
  dessert_button.style.background = '#F2E8CF';
  pizza_button.style.background = '#6a994e';
  salad_button.style.background = '#6a994e';
  pasta_button.style.background = '#6a994e';
  drinks_button.style.background = '#6a994e';
  for (let i = 0; i < dessert.length; i++) {
    pizza[i].style.display = 'none';
    salad[i].style.display = 'none';
    pasta[i].style.display = 'none';
    dessert[i].style.display = 'block';
    drinks[i].style.display = 'none';
  }
};
drinks_button.onclick = function () {
  drinks_button.style.background = '#F2E8CF';
  pizza_button.style.background = '#6a994e';
  dessert_button.style.background = '#6a994e';
  salad_button.style.background = '#6a994e';
  pasta_button.style.background = '#6a994e';
  for (let i = 0; i < dessert.length; i++) {
    pizza[i].style.display = 'none';
    salad[i].style.display = 'none';
    pasta[i].style.display = 'none';
    dessert[i].style.display = 'none';
    drinks[i].style.display = 'block';
  }
};
closeModalButton.addEventListener('click', hideModalWindow);
openModalButton.addEventListener('click', showModalWindow);
modalWindowOverlay.addEventListener('click', hideModalWindowOnBlur);

//cart
const shoppingCart = (function () {
  // =============================
  // Private methods and propeties
  // =============================
  cart = [];

  // Constructor
  function Item(name, price, count) {
    this.name = name;
    this.price = price;
    this.count = count;
  }

  // Save cart
  function saveCart() {
    sessionStorage.setItem('shoppingCart', JSON.stringify(cart));
  }

  // Load cart
  function loadCart() {
    cart = JSON.parse(sessionStorage.getItem('shoppingCart'));
  }
  if (sessionStorage.getItem('shoppingCart') != null) {
    loadCart();
  }

  // =============================
  // Public methods and propeties
  // =============================
  let obj = {};

  // Add to cart
  obj.addItemToCart = function (name, price, count) {
    for (let item in cart) {
      if (cart[item].name === name) {
        cart[item].count++;
        saveCart();
        return;
      }
    }
    let item = new Item(name, price, count);
    cart.push(item);
    saveCart();
  };
  // Set count from item
  obj.setCountForItem = function (name, count) {
    for (let i in cart) {
      if (cart[i].name === name) {
        cart[i].count = count;
        break;
      }
    }
  };
  // Remove item from cart
  obj.removeItemFromCart = function (name) {
    for (let item in cart) {
      if (cart[item].name === name) {
        cart[item].count--;
        if (cart[item].count === 0) {
          cart.splice(item, 1);
        }
        break;
      }
    }
    saveCart();
  };

  // Remove all items from cart
  obj.removeItemFromCartAll = function (name) {
    for (let item in cart) {
      if (cart[item].name === name) {
        cart.splice(item, 1);
        break;
      }
    }
    saveCart();
  };

  // Clear cart
  obj.clearCart = function () {
    cart = [];
    saveCart();
  };

  // Count cart
  obj.totalCount = function () {
    let totalCount = 0;
    for (let item in cart) {
      totalCount += cart[item].count;
    }
    return totalCount;
  };

  // Total cart
  obj.totalCart = function () {
    let totalCart = 0;
    for (let item in cart) {
      totalCart += cart[item].price * cart[item].count;
    }
    return Number(totalCart.toFixed(2));
  };

  // List cart
  obj.listCart = function () {
    let cartCopy = [];
    for (i in cart) {
      let item = cart[i];
      itemCopy = {};
      for (p in item) {
        itemCopy[p] = item[p];
      }
      itemCopy.total = Number(item.price * item.count).toFixed(2);
      cartCopy.push(itemCopy);
    }
    return cartCopy;
  };

  // cart : Array
  // Item : Object/Class
  // addItemToCart : Function
  // removeItemFromCart : Function
  // removeItemFromCartAll : Function
  // clearCart : Function
  // countCart : Function
  // totalCart : Function
  // listCart : Function
  // saveCart : Function
  // loadCart : Function
  return obj;
})();

// *****************************************
// Triggers / Events
// *****************************************
// Add item
$('.add-to-cart').click(function (event) {
  event.preventDefault();
  let name = $(this).data('name');
  let price = Number($(this).data('price'));
  shoppingCart.addItemToCart(name, price, 1);
  console.log(cart);
  displayCart();
});

// Clear items
$('.clear-cart').click(function () {
  shoppingCart.clearCart();
  displayCart();
});

function displayCart() {
  let cartArray = shoppingCart.listCart();
  let output = '';
  for (let i in cartArray) {
    output +=
      '<tr>' +
      '<td>' +
      cartArray[i].name +
      '</td>' +
      '<td>(' +
      cartArray[i].price +
      ')</td>' +
      "<td><div class='input-group'><button class='minus-item input-group-addon btn btn-primary' data-name=" +
      cartArray[i].name +
      '>-</button>' +
      "<input type='number' class='item-count form-control' data-name='" +
      cartArray[i].name +
      "' value='" +
      cartArray[i].count +
      "'>" +
      "<button class='plus-item btn btn-primary input-group-addon' data-name=" +
      cartArray[i].name +
      '>+</button></div></td>' +
      "<td><button class='delete-item btn btn-danger' data-name=" +
      cartArray[i].name +
      '>X</button></td>' +
      ' = ' +
      '<td>' +
      cartArray[i].total +
      '</td>' +
      '</tr>';
  }
  $('.show-cart').html(output);
  $('.total-cart').html(shoppingCart.totalCart());
  $('.total-count').html(shoppingCart.totalCount());
}

// Delete item button

$('.show-cart').on('click', '.delete-item', function () {
  let name = $(this).data('name');
  shoppingCart.removeItemFromCartAll(name);
  displayCart();
});

// -1
$('.show-cart').on('click', '.minus-item', function () {
  let name = $(this).data('name');
  shoppingCart.removeItemFromCart(name);
  displayCart();
});
// +1
$('.show-cart').on('click', '.plus-item', function () {
  let name = $(this).data('name');
  shoppingCart.addItemToCart(name);
  displayCart();
});

// Item count input
$('.show-cart').on('change', '.item-count', function () {
  let name = $(this).data('name');
  let count = Number($(this).val());
  shoppingCart.setCountForItem(name, count);
  displayCart();
});

displayCart();


$(document).ready( function() {
  $('#order-now').click(function() {
  $.ajax({
    type: 'POST',
    contentType: 'application/json',
    data: JSON.stringify(formdata),
    dataType: 'json',
    url: 'http://145.93.177.83:5000/index',
    success: function (e) {
      console.log(e);
      shoppingCart.clearCart();
      window.location = '';
    },
    error: function (error) {
      console.log(error);
    },
  });
}



// document.getElementById('order-now').addEventListener('click', postData());
