// sessionUtils.js
function getSessionUserId() {
    const userId = sessionStorage.getItem('user_id');
    if (!userId) {
        throw new Error("User ID not found in session storage");
    }
    
    return userId;
}

export { getSessionUserId };
