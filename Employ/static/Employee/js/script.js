

function slider(anything) {
    document.querySelector('.one').src = anything;
  };
  
  let menu = document.querySelector('#menu-icon');
  let navbar = document.querySelector('.navbar');
  
  menu.onclick = () => {
    menu.classList.toggle('bx-x');
    navbar.classList.toggle('open');
  }
  
  $(document).ready(function () {
    $(window).scroll(function () {
      if ($(window).scrollTop() + $(window).height() == $(document).height()) {
        $('header').addClass('hidden');
      } else {
        $('header').removeClass('hidden');
      }
    });
  });

     // JavaScript code to close the pop-up after a delay
     setTimeout(function() {
      document.querySelector('.popup').style.display = 'none';
    }, 3000);


    document.addEventListener("DOMContentLoaded", function() {
      const links = document.querySelectorAll(".sidebar a");
      const sections = document.querySelectorAll(".section");
    
      links.forEach(function(link) {
        link.addEventListener("click", function(e) {
          e.preventDefault();
    
          const sectionId = this.getAttribute("data-section");
          const section = document.getElementById(sectionId);
    
          sections.forEach(function(section) {
            section.style.display = "none";
          });
    
          section.style.display = "block";
        });
      });
    });
    

    


    // document.getElementById('signup-form').addEventListener('submit', function(event) {
    //   event.preventDefault();
    
    //   // Retrieve form values
    //   var username = document.getElementById('username').value;
    //   var password = document.getElementById('password').value;
    //   var email = document.getElementById('email').value;
    //   var csrfToken = document.getElementsByName('csrfmiddlewaretoken')[0].value; // Get the CSRF token value

    
    //   // Send the data to the server (e.g., using AJAX)
    //   // You can use JavaScript fetch API or any other AJAX library
    
    //   // Example using fetch API
    //   fetch('/signup', {
    //     method: 'POST',
    //     headers: {
    //       'Content-Type': 'application/json',
    //       'X-CSRFToken': csrfToken // Include the CSRF token in the request header
    //     },
    //     body: JSON.stringify({
    //       username: username,
    //       password: password,
    //       email: email
    //     })
    //   })
    //   .then(response => response.json())
    //   .then(data => {
    //     // Handle the response from the server
    //     // You can redirect the user to a success page or display a message
    //     console.log(data);
    //   })
    //   .catch(error => {
    //     // Handle any errors that occurred during the request
    //     console.error(error);
    //   });
    // });

    
    // document.getElementById('signin-form').addEventListener('submit', function(event) {
    //   event.preventDefault();
    
    //   // Retrieve form values
    //   var username = document.getElementById('username').value;
    //   var password = document.getElementById('password').value;
    
    //   // Send the data to the server (e.g., using AJAX)
    //   // You can use JavaScript fetch API or any other AJAX library
    
    //   // Example using fetch API
    //   fetch('/signin', {
    //     method: 'POST',
    //     headers: {
    //       'Content-Type': 'application/json'
    //     },
    //     body: JSON.stringify({
    //       username: username,
    //       password: password
    //     })
    //   })
    //   .then(response => response.json())
    //   .then(data => {
    //     // Handle the response from the server
    //     // You can redirect the user to the home page or display a message
    //     console.log(data);
    //   })
    //   .catch(error => {
    //     // Handle any errors that occurred during the request
    //     console.error(error);
    //   });
    // });
    