// 구매하려는 모든 상품의 할인가격을 합해서 '총 상품 금액' 구하기
const discountedPrices = document.querySelectorAll('.pdt-pay')
const buyMounts = document.querySelectorAll('.pdt-buy-mount')
const totPrice = document.querySelector('#tot-price')

let sumPrice = 0
for (i = 0; i < discountedPrices.length; i++) {
  sumPrice += parseInt(discountedPrices[i].dataset.discountedPrice) * parseInt(buyMounts[i].dataset.mount)
}

totPrice.innerText = `${sumPrice.toLocaleString()}원`



// 구매하려는 모든 상품의 배송비를 합해서 '총 베송비' 구하기
const deliveries = document.querySelectorAll('.pdt-delivery')
const totDelivery = document.querySelector('#tot-delivery')

let sumDeliveries = 0
for (let delivery of deliveries) {
  sumDeliveries += parseInt(delivery.dataset.delivery)
}

totDelivery.innerText = `${sumDeliveries.toLocaleString()}원`



// '총 상품 금액'과 '총 배송비'를 합해서 '최종 결제 금액' 구하기
const finalPayments = document.querySelectorAll('.final-payment > span')

for (let finalPayment of finalPayments) {
  finalPayment.innerText = `${(sumPrice + sumDeliveries).toLocaleString()}`
}



// 카카오 결제
// iamport 참고: https://docs.iamport.kr/implementation/payment
const kakaoPayForm = document.querySelector('#pay-form')
const pdtNames = document.querySelectorAll('.pdt-name')
const username = document.querySelector('#username').value
const userEmail = document.querySelector('#email').value

kakaoPayForm.addEventListener('submit', function (event) {
  console.log('왔니')
  event.preventDefault()
  requestPay()
})

if (pdtNames.length > 1) {
  var name = `${pdtNames[0]} 외 ${pdtNames.length}개`
} else {
  var name = `${pdtNames[0]}`
}

var IMP = window.IMP; // 생략 가능
IMP.init("imp82035714"); // 예: imp00000000
function requestPay() {
  console.log('함수 실행됐니?')
  // IMP.request_pay(param, callback) 결제창 호출
  IMP.request_pay({ // param
    pg: "kakaopay.TC0ONETIME",
    pay_method: "card",
    merchantuid: "merchant" + new Date().getTime(),
    name: (pdtNames.length > 1) ? `${pdtNames[0].innerText} 외 ${pdtNames.length}개` : `${pdtNames[0].innerText}`,
    amount: finalPayments[0].innerText,
    buyer_email: userEmail,
    buyer_name: username,
    // buyer_tel: "010-4242-4242",
    // buyer_addr: "서울특별시 강남구 신사동",
    // buyer_postcode: "01181"
  }, function (rsp) { // callback
    if (rsp.success) {
      jQuery.ajax({
        url: "https://www.myservice.com/payments/complete", // 가맹점 서버
        method: "POST",
        headers: { "Content-Type": "application/json" },
        data: {
          imp_uid: rsp.imp_uid,
          merchant_uid: rsp.merchant_uid
          //기타 필요한 데이터가 있으면 추가 전달
        }
      }).done(function (data) {
        // 가맹점 서버 결제 API 성공시 로직
      })
      alert('결제 완료!')
      const translateForm = document.querySelector('#translate-form')
      translateForm.submit()
      // var link = windows.location.protocol + windows.location.host + '/complete/';
      // console.log(link)
      // window.location.href = link;
      // window.location.replace(link);
      // window.open(link);
    } else {
      alert('결제 실패')
    }
  });
}


