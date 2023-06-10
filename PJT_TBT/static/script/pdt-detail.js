// 일단 첫 화면은 가장 첫번째 상품 이미지가 active
// 왼쪽 작은 상품 이미지 클릭했을 때, 오른쪽 큰 이미지로 보이게
const pdtImages = document.querySelectorAll('.pdt-img');
const pdtFirstImage = document.querySelector('.pdt-first-img');
const glass = document.querySelector('.img-magnifier-glass');

const src = pdtFirstImage.src;
let defaultSource = src;
glass.style.backgroundImage = "url('" + defaultSource + "')";

pdtImages[0].classList.add('active');

for (let pdtImage of pdtImages) {
  pdtImage.addEventListener('click', function (event) {
    for (let img of pdtImages) {
      img.classList.remove('active');
    }
    event.target.classList.add('active');
    clickedImgSrc = event.target.getAttribute('src');
    pdtFirstImage.setAttribute('src', clickedImgSrc);
    glass.style.backgroundImage = "url('" + clickedImgSrc + "')";
  });
}

// 이미지 확대
function magnify(zoom) {
  let img, w, h, bw;

  img = document.querySelector('#myimage');

  glass.style.backgroundRepeat = 'no-repeat';
  glass.style.backgroundSize =
    img.width * zoom + 'px ' + img.height * zoom + 'px';
  bw = 3;
  w = glass.offsetWidth / 2;
  h = glass.offsetHeight / 2;

  glass.addEventListener('mousemove', moveMagnifier);
  img.addEventListener('mousemove', moveMagnifier);

  glass.addEventListener('touchmove', moveMagnifier);
  img.addEventListener('touchmove', moveMagnifier);
  function moveMagnifier(e) {
    let pos, x, y;

    e.preventDefault();

    pos = getCursorPos(e);
    x = pos.x;
    y = pos.y;

    if (x > img.width - w / zoom) {
      x = img.width - w / zoom;
    }
    if (x < w / zoom) {
      x = w / zoom;
    }
    if (y > img.height - h / zoom) {
      y = img.height - h / zoom;
    }
    if (y < h / zoom) {
      y = h / zoom;
    }

    glass.style.left = x - w + 'px';
    glass.style.top = y - h + 'px';

    glass.style.backgroundPosition =
      '-' + (x * zoom - w + bw) + 'px -' + (y * zoom - h + bw) + 'px';
  }

  function getCursorPos(e) {
    let a,
      x = 0,
      y = 0;
    e = e || window.event;

    a = img.getBoundingClientRect();

    x = e.pageX - a.left;
    y = e.pageY - a.top;

    x = x - window.pageXOffset;
    y = y - window.pageYOffset;
    return { x: x, y: y };
  }
}

magnify(2);

// 별점 소수점으로 채우기
const starsColorAll = document.querySelectorAll('.stars-color');

for (let starsColor of starsColorAll) {
  avgOfGrade = starsColor.dataset.avgGrade ? starsColor.dataset.avgGrade : 0;
  starsColor.style.width = `${(avgOfGrade / 5) * 118}px`;
  //console.log(starsColor)
  //console.log(starsColor.style.width)
}

// 주문 금액 기본값 넣기 (수량 default=1일 때 주문 금액)
const totalPurchasePrice = document.querySelector('.total-purchase-price');
const deliveryPrice = parseInt(totalPurchasePrice.dataset.delivery);
const pdtPrice = parseInt(totalPurchasePrice.dataset.price);
const sale = parseInt(totalPurchasePrice.dataset.sale);

totalPurchasePrice.innerText = `${(
  pdtPrice * (100 - sale) * 0.01 * 1 +
  deliveryPrice
).toLocaleString('ko-KR')}원`;

// 수량 버튼을 눌렀을 때 수량 증감 및 주문 금액 계산
// 장바구니/바로구매 버튼에 수량 정보 넘기기
// 수량=0일때, 장바구니/바로구매 버튼 누르면 모달창 뜨게
const minusBtn = document.querySelector('.minus-btn');
const plusBtn = document.querySelector('.plus-btn');
const buyMount = document.querySelector('.buy-mount');

const basketBtnInputMounts = document.querySelectorAll('.basket-btn-mount');
const mountPerPdtInputs = document.querySelectorAll('.mount_per_pdt');

const basketBtnModals = document.querySelectorAll('.basket-btn-modal');
const basketBtnSubmits = document.querySelectorAll('.basket-btn-submit');
const buyBtnModals = document.querySelectorAll('.buy-btn-modal');
const buyBtnSubmits = document.querySelectorAll('.buy-btn-submit');

const calTotPurchasePrice = function (mount) {
  // 주문 금액 구하기
  if (mount !== 0) {
    totalPurchasePrice.innerText = `${(
      pdtPrice * (100 - sale) * 0.01 * mount +
      deliveryPrice
    ).toLocaleString('ko-KR')}원`;
  } else {
    totalPurchasePrice.innerText = '0원';
  }
};

const mount0ActiveModal = function (mount) {
  // 수량=0이면 모달창 띄움
  if (mount === 0) {
    for (let basketBtnSubmit of basketBtnSubmits) {
      basketBtnSubmit.classList.remove('active');
    }
    for (let basketBtnModal of basketBtnModals) {
      basketBtnModal.classList.add('active');
    }
    for (let buyBtnSubmit of buyBtnSubmits) {
      buyBtnSubmit.classList.remove('active');
    }
    for (let basketBtnModal of buyBtnModals) {
      basketBtnModal.classList.add('active');
    }
  } else {
    for (let basketBtnModal of basketBtnModals) {
      basketBtnModal.classList.remove('active');
    }
    for (let basketBtnSubmit of basketBtnSubmits) {
      basketBtnSubmit.classList.add('active');
    }
    for (let buyBtnModal of buyBtnModals) {
      buyBtnModal.classList.remove('active');
    }
    for (let buyBtnSubmit of buyBtnSubmits) {
      buyBtnSubmit.classList.add('active');
    }
  }
};

plusBtn.addEventListener('click', function () {
  buyMount.innerText = parseInt(buyMount.innerText) + 1;
  let mount = parseInt(buyMount.innerText);
  calTotPurchasePrice(mount);
  for (let basketBtnInputMount of basketBtnInputMounts) {
    basketBtnInputMount.value = mount;
  }
  for (let mountPerPdtInput of mountPerPdtInputs) {
    mountPerPdtInput.value = mount;
  }
  mount0ActiveModal(mount);
});

minusBtn.addEventListener('click', function () {
  if (parseInt(buyMount.innerText) - 1 >= 0) {
    buyMount.innerText = parseInt(buyMount.innerText) - 1;
  }
  let mount = parseInt(buyMount.innerText);
  calTotPurchasePrice(mount);
  for (let basketBtnInputMount of basketBtnInputMounts) {
    basketBtnInputMount.value = mount;
  }
  for (let mountPerPdtInput of mountPerPdtInputs) {
    mountPerPdtInput.value = mount;
  }
  mount0ActiveModal(mount);
});

// 상품정보/리뷰/문의/추천 탭 클릭 시, 클래스에 active 추가
const tabs = document.querySelectorAll('.tab');

tabs.forEach(function (tab) {
  tab.addEventListener('click', function (event) {
    for (let tab of tabs) {
      tab.classList.remove('active');
    }
    event.currentTarget.classList.add('active');
    console(event.currentTarget);
  });
});

// 각 리뷰의 평점 갯수에 따라 grade-bar 채우기
const gradeBarColorAll = document.querySelectorAll('.grade-bar-color-wrap');
const gradeCounts = document.querySelectorAll('.pdt-review-grade-count');

let totCounts = 0;
for (let gradeCount of gradeCounts) {
  totCounts += parseInt(gradeCount.innerText);
}

for (i = 0; i < 5; i++) {
  if (totCounts === 0) {
    gradeBarColorAll[i].style.width = `0px`;
  } else {
    gradeBarColorAll[i].style.width = `${
      (160 * parseInt(gradeCounts[i].innerText)) / totCounts
    }px`;
  }
}
