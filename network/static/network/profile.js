document.addEventListener('DOMContentLoaded', function() {
    // Select all buttons
    let unfollowBtn = document.querySelector('#unfollowBtn')
    if (unfollowBtn !== null) {
        unfollowBtn.onmouseover = function () {
            unfollowBtn.value = "Unfollow"
            unfollowBtn.className = "btn following-btn"
            unfollowBtn.style.backgroundColor = "#c90d00"
        }
        unfollowBtn.onmouseout = function () {
            unfollowBtn.value = "Following"
            unfollowBtn.className = "btn following-btn"
            unfollowBtn.style.backgroundColor = "rgba(29,161,242,1.00)"
        }
    }

});