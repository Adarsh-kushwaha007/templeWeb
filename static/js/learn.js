// document.addEventListener('DOMContentLoaded', function() {
//     const feedbackForm = document.getElementById('feedback-form');
//     const feedbackTextArea = document.getElementById('feedback');
//     const feedbackMessage = document.getElementById('feedback-message');
  
//     feedbackForm.addEventListener('submit', function(event) {
//       event.preventDefault();
  
//       const feedback = feedbackTextArea.value.trim();
  
//       if (feedback === '') {
//         displayFeedbackMessage('Please enter your feedback.', 'error');
//       } else {
//         // Here you can implement your logic to send the feedback to your backend or handle it as you wish
//         displayFeedbackMessage('Feedback submitted successfully!', 'success');
//         // Optionally, you can clear the textarea after submitting feedback
//         feedbackTextArea.value = '';
//       }
//     });
  
//     function displayFeedbackMessage(message, type) {
//       feedbackMessage.textContent = message;
  
//       if (type === 'success') {
//         feedbackMessage.style.color = 'green';
//       } else if (type === 'error') {
//         feedbackMessage.style.color = 'red';
//       }
//     }
//   });
  
document.addEventListener('DOMContentLoaded', function() {
  const feedbackForm = document.getElementById('feedback-form');
  const feedbackTextArea = document.getElementById('feedback');
  const feedbackMessage = document.getElementById('feedback-message');

  feedbackForm.addEventListener('submit', function(event) {
      event.preventDefault();

      const feedback = feedbackTextArea.value.trim();

      if (feedback === '') {
          displayFeedbackMessage('Please enter your feedback.', 'error');
      } else {
          // Send the feedback data to the backend server
          sendFeedback(feedback);
      }
  });

  function sendFeedback(feedback) {
    const csrftoken = getCookie('csrftoken');
      // Construct the request body
    //   const requestBody = JSON.stringify({ content: feedback });
      
      // Make an AJAX request to the backend endpoint
      fetch('/submit_feedback', {
          method: 'POST',
          headers: {
              'Content-Type': 'application/json',
              'X-CSRFToken' : csrftoken
          },
          body: requestBody
      })
      .then(response => {
          if (response.ok) {
              return response.json();
          } else {
              throw new Error('Failed to submit feedback');
          }
      })
      .then(data => {
          // Handle the successful response from the server
          displayFeedbackMessage('Feedback submitted successfully!', 'success');
          feedbackTextArea.value = ''; // Clear the textarea
      })
      .catch(error => {
          // Handle errors or failed requests
          console.error('Error:', error);
          displayFeedbackMessage('Failed to submit feedback. Please try again later.', 'error');
      });
  }

  function displayFeedbackMessage(message, type) {
      feedbackMessage.textContent = message;

      if (type === 'success') {
          feedbackMessage.style.color = 'green';
      } else if (type === 'error') {
          feedbackMessage.style.color = 'red';
      }
  }
  // Function to get CSRF token from cookie
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Check if the cookie contains the desired name
            if (cookie.startsWith(name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
    }
});

