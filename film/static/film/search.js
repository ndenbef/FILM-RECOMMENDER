$(function() {
    var $searchInput = $('#searches');
    var $searchButton = $('#search-btn');

    function togglePopover() {
        var showPopover = $searchInput.val().trim() === '';
        $searchButton.popover(showPopover ? 'show' : 'hide');
    }

    $searchInput.keyup(togglePopover);
    $searchButton.click(function(event) {
        if ($searchInput.val().trim() === '') {
            $(this).popover('show');
            event.preventDefault();
        }
    });
});

$(function() {
    $('#submit-btn').click(function(e) {
        // Prevent default form submission behavior
        e.preventDefault();

        // Get the value of the input field
        var name = $('#name').val().trim();

        // Check if the input field is empty
        if (name === '') {
            // Show popover with error message
            $('#name').popover({
                content: 'Please enter a name',
                placement: 'top'
            }).popover('show');
        } else {
            // Build query string with form data
            var form_data = $(this).closest('form').serialize();

            // Redirect to the URL with the query string
            window.location.href = '{% url "my_view" %}' + '?' + form_data;
        }
    });
});