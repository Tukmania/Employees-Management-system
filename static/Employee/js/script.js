

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

    function showSection(sectionNumber) {
      // Hide all content sections
      var sections = document.getElementsByClassName('content-section');
      for (var i = 0; i < sections.length; i++) {
        sections[i].style.display = 'none';
      }

      // Show the selected content section
      var selectedSection = document.getElementById('section' + sectionNumber);
      selectedSection.style.display = 'block';

      // Remove 'active' class from all sidebar links
      var sidebarLinks = document.getElementsByTagName('a');
      for (var i = 0; i < sidebarLinks.length; i++) {
        sidebarLinks[i].classList.remove('active');
      }

      // Add 'active' class to the clicked sidebar link
      var clickedLink = document.querySelector('[onclick="showSection(' + sectionNumber + ')"]');
      clickedLink.classList.add('active');
    }

    


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
    