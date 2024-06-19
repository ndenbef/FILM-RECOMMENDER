  $(function() {
      // select the form by ID and add an event listener to the submit button
      $('#registration-form').on('submit', function() {
          // get all checked checkboxes and join their values with a comma
          var selectedValues = $('input[name="genre"]:checked').map(function() {
              return this.value;
          }).get().join(',');
          // set the value of a hidden field to the joined selected values
          $('<input>').attr({
              type: 'hidden',
              name: 'selected_genres',
              value: selectedValues
          }).appendTo('#registration-form');
      });
  });