// ----- 분류 필터 -----
// 현재 필터에 따라 해당 dropdown-item에만 active 붙이기
const filter = document.querySelector('.pdt-filter').dataset.filter
const dropdownItems = document.querySelectorAll('.dropdown-item')
const filterType = {
  'register': 0,
  'high-sale': 1,
  'high-price': 2,
  'low-price': 3,
}

for (i = 0; i < dropdownItems.length; i++) {
  dropdownItems[i].classList.remove('active')
}

const filterIdx = filterType[filter]
dropdownItems[filterIdx].classList.add('active')

// 현재 active한 필터의 text를 버튼 text와 동일하게 설정
const dropdownBtn = document.querySelector('.dropdown-toggle')
const activeDropdownItem = document.querySelector('.dropdown-item.active')

dropdownBtn.innerText = activeDropdownItem.innerText

// 현재 크리스마스 카테고리에 따라 해당 xmas-btn에만 active 붙이기
const xmasBtns = document.querySelectorAll('.xmas-btn')
const xmasCategory = document.querySelector('#xmas-category').value
const xmasCategoryType = {
  'card': 0,
  'wreath': 1,
  'decoration': 2,
}

for (i = 0; i < xmasBtns.length; i++) {
  xmasBtns[i].classList.remove('active')
}

const xmasCategoryIdx = xmasCategoryType[xmasCategory]
xmasBtns[xmasCategoryIdx].classList.add('active')
