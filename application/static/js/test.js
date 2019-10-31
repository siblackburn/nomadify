const createMessageWrappers = (message) => {
    let message_wrap = document.createElement('div') //<div>
    message_wrap.classList.add('message-wrap'); //<div class="message-wrap"> //
    message_out.classList.add('message','out'); //<div class="message out"> //

    let mssg = document.createElement('p') //<p>
    mssg.classList.add('mssg'); //<p class="mssg"> //
    mssg.innerHTML = message.message_content