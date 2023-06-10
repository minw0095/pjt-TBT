'use strict';

const form = document.querySelector('#follow-form');

const revModal = document.querySelector('#review');
const qnaModal = document.querySelector('#qna');

const overlay = document.querySelector('.overlayC');
const revBtnCloseModal = document.querySelector('.btn-close-rev');
const qnaBtnCloseModal = document.querySelector('.btn-close-qna');
const revBtnOpenModal = document.querySelector('#rev-modal-btn');
const qnaBtnOpenModal = document.querySelector('.qna-modal-btn');
const body = document.querySelector('body');

const revUpdateForm = document.querySelector('#review-form-update');
const revUpdateModal = document.querySelector('#review_update');
const revOpenUpdateBtns = document.querySelectorAll('.btn-modal-update');
const revCloseUpdateBtn = document.querySelector('.btn-close-rev-update');

const qnaUpdateForm = document.querySelector('#qna-form-update');
const qnaUpdateModal = document.querySelector('#qna_update');
const qnaOpenUpdateBtns = document.querySelectorAll('.btn-modal-update-qna');
const qnaCloseUpdateBtn = document.querySelector('.btn-close-qna-update');


const alertModal = document.querySelector('.rev-alert');
const alertOpenBtns = document.querySelectorAll('.btn-modal-delete');
const alertCloseBtns = document.querySelectorAll('.btn-cancel');
const alertDeleteBtn = document.querySelector('.btn-delete');

const alertOpenBtnsQna = document.querySelectorAll('.btn-modal-delete-qna');
const alertDeleteBtnQna = document.querySelector('.btn-delete-qna');
const alertModalQna = document.querySelector('.qna-alert');

// // const thumbsOverlay = document.querySelectorAll('.overlayC2');
// // const thumbsImgPop = document.querySelectorAll('.rev-body .rev-img-popup');
const thumbsImg = document.querySelectorAll('.rev-body .rev-img');
const thumbsCloseBtn = document.querySelectorAll('.rev-body .btn-close-img');

const topBtn = document.querySelector('#top');
window.addEventListener('scroll', function () {
    // console.log(this.scrollY);
    if (this.scrollY > 200) {
        topBtn.classList.add('on');
        topBtn.classList.remove('off');
    }
    else {
        topBtn.classList.remove('on');
        topBtn.classList.add('off');
    }
});
topBtn.addEventListener('click', function (e) {
    e.preventDefault();
    window.scrollTo({ top: 0, behavior: 'smooth' });
})

// 경고 모달창
try {
    const openAlert = function (e) {
        e.preventDefault();
        // console.log(e.target.href);
        alertModal.classList.remove('hidden');
        overlay.classList.remove('hidden');
        body.classList.add('scroll-block');

        let urls = e.target.href;
        // if (!alertDeleteBtn) return;
        alertDeleteBtn.setAttribute('href', `${urls}`);

    }

    const closeAlert = function (e) {
        e.preventDefault();
        alertModal.classList.add('hidden');
        overlay.classList.add('hidden');
        body.classList.remove('scroll-block');
    }

    alertOpenBtns.forEach(alertBtn => {
        alertBtn.addEventListener('click', openAlert)
    });
    alertCloseBtns.forEach(alertClose => {
        alertClose.addEventListener('click', closeAlert);
    })



    const openAlertQna = function (e) {
        e.preventDefault();
        console.log(e.target.href);
        alertModalQna.classList.remove('hidden');
        overlay.classList.remove('hidden');
        body.classList.add('scroll-block');

        let urls = e.target.href;
        // if (!alertDeleteBtn) return;
        alertDeleteBtnQna.setAttribute('href', `${urls}`);
    }

    const closeAlertQna = function (e) {
        e.preventDefault();
        alertModalQna.classList.add('hidden');
        overlay.classList.add('hidden');
        body.classList.remove('scroll-block');
    }

    alertOpenBtnsQna.forEach(alertBtn => {
        alertBtn.addEventListener('click', openAlertQna);
    });
    alertCloseBtns.forEach(alertClose => {
        alertClose.addEventListener('click', closeAlertQna);
    })


} catch {

}
//  리뷰 썸네일 이미지 팝업
try {
    const imgPopup = function (e) {
        const overlay = e.target.nextElementSibling;
        // console.log(overlay.children[1]);
        overlay.classList.remove('hidden');
        overlay.children[1].classList.remove('hidden');
        body.classList.add('scroll-block');

    }
    const imgClose = function (e) {
        const overlay = e.target.parentElement.parentElement;
        overlay.classList.add('hidden');
        body.classList.remove('scroll-block');
    }

    thumbsImg.forEach(img => {
        img.addEventListener('click', imgPopup);
    })
    thumbsCloseBtn.forEach(close => {
        close.addEventListener('click', imgClose);
    })

} catch {

}

// 리뷰, 문의 모달창
try {

    revBtnOpenModal.addEventListener('click', function (e) {
        e.preventDefault();
        revModal.classList.remove('hidden');
        overlay.classList.remove('hidden');
        body.classList.add('scroll-block');
    });
    qnaBtnOpenModal.addEventListener('click', function () {
        qnaModal.classList.remove('hidden');
        overlay.classList.remove('hidden');
        body.classList.add('scroll-block');
    });
    revBtnCloseModal.addEventListener('click', function () {
        revModal.classList.add('hidden');
        overlay.classList.add('hidden');
        body.classList.remove('scroll-block');
    });
    qnaBtnCloseModal.addEventListener('click', function () {
        qnaModal.classList.add('hidden');
        overlay.classList.add('hidden');
        body.classList.remove('scroll-block');
    });
    // overlay.addEventListener('click', function () {
    //     body.classList.remove('scroll-block');
    //     revModal.classList.add('hidden');
    //     qnaModal.classList.add('hidden');
    //     overlay.classList.add('hidden');
    // })


    document.addEventListener('keydown', function (e) {
        if (e.key === 'Escape' && !modal.classList.contains('hidden')) {
            body.classList.remove('scroll-block');
            revModal.classList.add('hidden');
            qnaModal.classList.add('hidden');
            overlay.classList.add('hidden')
        }
    });


    const tabCont = document.querySelector('.cate-area');
    const tabs = document.querySelectorAll('.tab_oper');

    tabCont.addEventListener('click', function (e) {
        const clicked = e.target.closest('.tab_oper');
        if (!clicked) return;
        tabs.forEach(t => t.classList.remove('tab-active'));
        clicked.classList.add('tab-active');
    });

} catch {

}

// 리뷰 수정 모달창
try {
    const openUpdateModal = function (e) {
        e.preventDefault();
        // console.log(e.target.href);
        revUpdateModal.classList.remove('hidden');
        overlay.classList.remove('hidden');
        body.classList.add('scroll-block');

        let urls = e.target.href;
        revUpdateForm.setAttribute('action', `${urls}`)
        // console.log(urls);
        let cnt = e.target.dataset.cnt
        cnt = Number(cnt)
        cnt++;
        console.log(urls);

        const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value
        console.log(csrftoken);

        axios({
            method: 'POST',
            url: `${urls}`,
            headers: {
                'X-CSRFToken': csrftoken,
                'Content-Type': 'multipart/form-data'
            }
        })
            .then(response => {
                const dataLength = response.data.length;
                const dataNum = cnt - dataLength;
                const formData = response.data[dataNum];
                const formTitle = formData.title;
                const formCont = formData.content;
                const formGrade = formData.grade;
                // const formImg = formData.review_image;
                // console.log(formTitle, formCont);
                const inputTitle = document.querySelector('#update-title');
                const inputCont = document.querySelector('#update-content');
                const inputGrade = document.querySelector(`#update-rate-${formGrade}`)
                const inputImg = document.querySelector('#file');

                inputTitle.setAttribute('value', `${formTitle}`);
                inputCont.innerText = formCont;
                inputGrade.checked = true;
                // inputImg.setAttribute('value', `${formImg}`);
            });
    }
    const closeUpdateModal = function () {
        revUpdateModal.classList.add('hidden');
        overlay.classList.add('hidden');
        body.classList.remove('scroll-block');
    }

    revOpenUpdateBtns.forEach(updateBtn => {
        updateBtn.addEventListener('click', openUpdateModal)
    });

    revCloseUpdateBtn.addEventListener('click', closeUpdateModal);

} catch {

}

// 문의 수정 모달창
// try {
//     const openUpdateModal = function (e) {
//         e.preventDefault();
//         // console.log(e.target.href);
//         qnaUpdateModal.classList.remove('hidden');
//         overlay.classList.remove('hidden');
//         body.classList.add('scroll-block');

//         let urls = e.target.href;
//         qnaUpdateForm.setAttribute('action', `${urls}`)
//         // console.log(urls);
//         let cnt = e.target.dataset.cnt
//         cnt = Number(cnt)
//         cnt++;
//         const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value

//         axios({
//             method: 'POST',
//             url: `${urls}`,
//             headers: {
//                 'X-CSRFToken': csrftoken,
//             }
//         })
//             .then(response => {
//                 console.log(response);
//                 // const dataLength = response.data.length;
//                 // const dataNum = cnt - dataLength;
//                 // console.log(dataNum);
//                 // const formData = response.data[dataNum];
//                 // console.log(formData);
//                 // const formCata = formData.category;
//                 // const formCont = formData.content;

//                 // const inputTitle = document.querySelector('#update-title');
//                 // const inputCont = document.querySelector('#update-content');


//                 //     inputTitle.setAttribute('value', `${formTitle}`);
//                 //     inputCont.innerText = formCont;
//                 //     inputGrade.checked = true;
//             });
//     }
//     const closeUpdateModal = function () {
//         qnaUpdateModal.classList.add('hidden');
//         overlay.classList.add('hidden');
//         body.classList.remove('scroll-block');
//     }

//     qnaOpenUpdateBtns.forEach(updateBtn => {
//         updateBtn.addEventListener('click', openUpdateModal)
//     });

//     qnaCloseUpdateBtn.addEventListener('click', closeUpdateModal);
// } catch {

// }

// 메인 인덱스 슬라이드
try {
    const slider = function () {
        const slides = document.querySelectorAll('.slide');
        const btnLeft = document.querySelector('.slider-btn-left');
        const btnRight = document.querySelector('.slider-btn-right');
        const dotContainer = document.querySelector('.dots');

        let curSlide = 0;
        const maxSlide = slides.length;

        const createDots = function () {
            slides.forEach(function (_, i) {
                dotContainer.insertAdjacentHTML('beforeend', `<button class="dots-dot" data-slide="${i}"></button>`);
            })
        };
        const activeDot = function (slide) {
            document.querySelectorAll('.dots-dot').forEach(dot => dot.classList.remove('dots-dot-active'));
            document.querySelector(`.dots-dot[data-slide="${slide}"]`).classList.add('dots-dot-active');
        };

        const goToSlide = function (slide) {
            slides.forEach((s, i) => s.style.transform = `translateX(${100 * (i - slide)}%)`);
        }

        const nextSlide = function () {
            if (curSlide === maxSlide - 1) {
                curSlide = 0;
            } else {
                curSlide++;
            }

            goToSlide(curSlide);
            activeDot(curSlide);
        };

        const prevSlide = function () {
            if (curSlide === 0) {
                curSlide = maxSlide - 1;
            } else {
                curSlide--;
            }

            goToSlide(curSlide);
            activeDot(curSlide);
        };
        const init = function () {
            createDots();
            goToSlide(0);
            activeDot(0);
        };

        init();

        btnLeft.addEventListener('click', prevSlide);
        btnRight.addEventListener('click', nextSlide);

        document.addEventListener('keydown', function (e) {
            if (e.key === "ArrowLeft") prevSlide();
            e.key === "ArrowRight" && nextSlide();
        });

        dotContainer.addEventListener('click', function (e) {
            if (e.target.classList.contains('dots-dot')) {
                const { slide } = e.target.dataset;
                goToSlide(slide);
                activeDot(slide);
            }
        });
        setInterval(nextSlide, 6000);
    };

    slider();
} catch {

}

// 유저 팔로우
try {

    form.addEventListener('submit', function (e) {
        e.preventDefault();
        const userId = e.target.dataset.userId;
        const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value

        axios({
            method: 'POST',
            url: `/accounts/${userId}/follow/`,
            headers: { 'X-CSRFToken': csrftoken, }
        })
            .then(response => {
                const isFollow = response.data.isFollow;
                const followBtn = document.querySelector('#follow-btn');
                if (isFollow === true) {
                    followBtn.innerText = 'unfollow'
                    followBtn.classList.remove('follow__btn');
                    followBtn.classList.add('unfollow__btn');
                } else {
                    followBtn.innerText = 'follow'
                    followBtn.classList.remove('unfollow__btn');
                    followBtn.classList.add('follow__btn');

                }
                const followersCount = document.querySelector('#followers-count');
                const followingsCount = document.querySelector('#followings-count');
                const followersCountValue = response.data.followers_count;
                const followingsCountValue = response.data.followings_count;
                followersCount.innerText = followersCountValue;
                followingsCount.innerText = followingsCountValue;
            })
    });

} catch {

}

// 리뷰 좋아요
const likeBtn = document.querySelectorAll(".like-btn");
try {

    const reviewlike = function (event) {
        // console.log(event.target.closest('.like-btn'));
        const reviewId = event.target.dataset.reviewId
        axios({
            method: 'get',
            url: `/reviews/${reviewId}/likes/`
        })
            .then((response) => {
                const isLiked = response.data.isLiked;
                if (isLiked === true) {
                    event.target.classList.add('bi-hand-thumbs-up-fill');
                    event.target.classList.remove('bi-hand-thumbs-up');
                    event.target.closest('.like-btn').classList.add('like-active');
                } else {
                    event.target.classList.add('bi-hand-thumbs-up');
                    event.target.classList.remove('bi-hand-thumbs-up-fill');
                    event.target.closest('.like-btn').classList.remove('like-active');

                }

                const likeCount = event.target.nextElementSibling;
                likeCount.innerText = response.data.likeCount;
            })
    }

    likeBtn.forEach(btn => {
        btn.addEventListener('click', reviewlike);
    })
} catch {

}
