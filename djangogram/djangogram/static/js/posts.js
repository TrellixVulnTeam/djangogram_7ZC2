const handleLikeClick = (buttonId) => {
    console.log(buttonId);

    const likeButton = document.getElementById(buttonId);
    console.log(likeButton);

    const likeIcon = likeButton.querySelector("i");
    console.log(likeIcon);
    likeIcon.classList.replace("fa-heart-o", "fa-heart")

    //서버로 좋아요 api호출
    //결과를 받고 html(좋아요 하트) 모습을 변경
}