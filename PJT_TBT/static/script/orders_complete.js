// 구매하려는 모든 상품의 할인가격을 합해서 '총 상품 금액' 구하기
const discountedPrices = document.querySelectorAll('.pdt-pay')
const buyMounts = document.querySelectorAll('.pdt-buy-mount')

let sumPrice = 0
for (i = 0; i < discountedPrices.length; i++) {
  sumPrice += parseInt(discountedPrices[i].dataset.discountedPrice) * parseInt(buyMounts[i].dataset.mount)
}



// 구매하려는 모든 상품의 배송비를 합해서 '총 베송비' 구하기
const deliveries = document.querySelectorAll('.pdt-delivery')

let sumDeliveries = 0
for (let delivery of deliveries) {
  sumDeliveries += parseInt(delivery.dataset.delivery)
}



// '총 상품 금액'과 '총 배송비'를 합해서 '최종 결제 금액' 구하기
const finalPayment = document.querySelector('.final-payment > span')

finalPayment.innerText = `${(sumPrice + sumDeliveries).toLocaleString()}`

