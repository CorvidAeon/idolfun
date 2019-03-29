function swapCostume(e, state){
    var card = e.closest(".card");
    var image = card.getElementsByTagName("img").item(0);//make card selector variable maybe?
    if (state=="regular") {
        image.src = image.dataset.regularSrc;
    } else if (state=="awk") {
        image.src = image.dataset.awkSrc;
    }
}
