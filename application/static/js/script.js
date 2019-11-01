let currentChatId = null;
let currentUserId = null;
const convo_info = document.querySelector('#convo-info');





// get the element that was clicked, this information is given to us in the click event; retrieve data- attributes
const convoClick = (event) => {
    const clickedElement = event.currentTarget;
    
    // clicked on item is greyed out rather than white, to designate which chat you're looking at
    for(let element of document.getElementsByClassName("convo")){
        element.classList.remove("active")
    }

    // adds the .active class to whatever is clicked on, so it's greyed out rather than white
    clickedElement.classList.add("active");    

    // populate form chat id input
    const dataAttributes = clickedElement.dataset;
    const chat_id = dataAttributes.chat_id;
    const user_id = dataAttributes.user_id;
    document.querySelector('#sndr-chat_id').value = chat_id;
    currentChatId = chat_id
    currentUserId = user_id

    // Retrieve the messages to populate main screen
    retrieveMessages(currentChatId, currentUserId);
}

    // looks for all "convo" classes, and adds an "eventlistener"; then if there is a "click" it runs convoClick
for(let element of document.getElementsByClassName("convo")) {
    element.addEventListener('click', convoClick, false);
}



    // gets JSON, then translates to JS, then runs addMessage function (with JS)
const retrieveMessages = (chat_id, user_id) => {
    const url = `/api/chats/${chat_id}/messages?user_id=${user_id}`
    fetch(url, {
        method: 'GET'
    })
    .then(response => response.json())
    .then(messages => {
        addMessages(messages)
    })
}







    // for each element in "message" run create messagewrapper
const addMessages = (messages) => {
    let MainWrapper = document.querySelector('#main-chat-wrap');
    MainWrapper.innerHTML = '';
    
    for(let message of messages) {
        createMessageWrappers(message)
    }
}

// auto refresh loads new messages if new messages come through
setInterval(() => {
    if(currentChatId !== null && currentUserId !== null) {
    retrieveMessages(currentChatId, currentUserId)
    }
}, 1000);




    // create a new wrapper for each message. If statement allows the colour to switch from green to white based on whether the user who's logged in has sent the message
const createMessageWrappers = (message) => {
    let message_wrap = document.createElement('div') //<div>
    message_wrap.classList.add('message-wrap'); //<div class="message-wrap"> //


    let message_in_out = document.createElement('div') //<div>
    const urlParams = new URLSearchParams(window.location.search)
    const user_id = urlParams.get('user_id');

    if (message.user.user_id == user_id) {
        message_in_out.classList.add('message','out');
    } else {
        message_in_out.classList.add('message','in');
    }



    let mssg = document.createElement('p') //<p>
    mssg.classList.add('mssg'); //<p class="mssg"> //
    mssg.innerHTML = message.message_content

    let mssg_time = document.createElement('p') //<p>
    mssg_time.classList.add('mssg-time'); //<p class="mssg-time"> //
    mssg_time.innerHTML = message.timestamp

    const MainWrapper = document.querySelector('#main-chat-wrap');
    message_in_out.appendChild(mssg)
    message_in_out.appendChild(mssg_time)
    message_wrap.appendChild(message_in_out)  
    MainWrapper.appendChild(message_wrap)
}





// First - get new message from newMessage function, get chat_id and user_id from the html form
const submitNewMessage = (event)  => {
    event.preventDefault();

    const newMessage = document.querySelector('#new-message').value;
    const chat_id = document.querySelector('#sndr-chat_id').value;
    const user_id = document.querySelector('#sndr-name').value;

    const url = `/api/chats/${chat_id}/messages?user_id=${user_id}`;
    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            'message_content': newMessage
        })
    })
    .then(res => {
        return res.json()
    })
    .then(data => {
        createMessageWrappers(data)
        document.querySelector('#new-message').value = '' 
        updateScroll()
        document.querySelector(`div.convo[data-chat_id="${chat_id}"] p.mssg`).innerHTML = data.message_content
        document.querySelector(`div.convo[data-chat_id="${chat_id}"] p.mssg`).innerHTML = data.timestamp
    })
}
// The then statement tells JS to execute each item in turn, rather than do asynchronus execution. This one returns JSON, then sets the send messages textbox to nothing, then posts the new message to the chat


// Function to make sure the chat always displays latest message in main-chat unless user scrolls up
function updateScroll(){
    var scrolldiv = document.getElementById("main-chat-wrap");
    scrolldiv.scrollTop = scrolldiv.scrollHeight;
}
setInterval(updateScroll,500);



// New groups popup form
function openForm() {
    document.getElementById("myForm").style.display = "block";
  }
  
  function closeForm() {
    document.getElementById("myForm").style.display = "none";
  }





  const createGroup = (event)  => {
    event.preventDefault();

    const newGroup = document.querySelector('#group-name').value;
    const user_ids = document.querySelector('#group-users').value;
    let user_ids = user_ids
    
    console.log(newGroup)
    console.log(user_ids)

    const url = `/api/new_group/`;
    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            'group_name': newGroup,
            'user_ids': user_ids
        })
    })
}