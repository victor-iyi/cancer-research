/**
 * @author Victor I. Afolabi
 *
 * A.I. Engineer & Software developer
 * javafolabi@gmail.com
 *
 * Created on 27 January, 2018 @ 3:01 AM.
 * Copyright © 2018. Victor. All rights reserved.
 */

(function ($) {
  
  $('.form-error').hide();

  $('#prediction-form').on('submit', function (e) {
    e.preventDefault();

    $.getJSON('/_classification', {

      algorithm: $('select#models').val(),
      clump_thickness: $('input[name="clump_thickness"]').val(),
      uniformity_of_cell_size: $('input[name="uniformity_of_cell_size"]').val(),
      uniformity_of_cell_shape: $('input[name="uniformity_of_cell_shape"]').val(),
      marginal_adhesion: $('input[name="marginal_adhesion"]').val(),
      single_epithelial_cell_size: $('input[name="single_epithelial_cell_size"]').val(),
      bare_nuclei: $('input[name="bare_nuclei"]').val(),
      bland_chromatin: $('input[name="bland_chromatin"]').val(),
      normal_nucleoli: $('input[name="normal_nucleoli"]').val(),
      mitoses: $('input[name="mitoses"]').val()

    }, function (data) {
      payload = data.payload;
      
      // Display error.
      if (payload.error !== null) {
        $('.form-error').show();
        $("p.error").text(payload.error);
        return;
      }

      // Clear error messages.
      $('.form-error').hide();
      $("p.error").text('');

      var $label = $('#cancer-result');

      // Display payload to the screen.
      $label.text(payload.prediction);
      $('#algorithm').text(payload.algorithm);

      // use appropriate class label
      if (payload.prediction.toString().toLowerCase() === 'benign')
        $label.addClass('label-success');
      else $label.addClass('label-danger');

      // Open prediction modal.
      $('#myModal').modal('show');
    });
  });


/*
 * +————————————————————————————————————————————————————————————————————————————————+
 * | +————————————————————————————————————————————————————————————————————————————+ |
 * | | Settings form.
 * | +————————————————————————————————————————————————————————————————————————————+ |
 * +————————————————————————————————————————————————————————————————————————————————+
 */
  $('#settings-form').on('submit', function (e) {
    e.preventDefault();
    
    var algorithm = $('select#models').val();
    var mode = $('select#mode').val();

    if (algorithm === '' || mode == '') {
      // Display error message.
      $('.form-error').show();
      $("p.error").text("All fields are required!");
    } else {
      // Everything went well...
      $.getJSON('/_settings', { algorithm: algorithm, mode: mode }, function (data) {
        payload = data.payload;

        // Display error.
        if (payload.error !== null) {
          $('.form-error').show();
          $("p.error").text(payload.error);
          return;
        }
        
        // Clear error messages.
        $('.form-error').hide();
        $("p.error").text('');
        
        // Update views.
        $('span#algorithm').text(payload.algorithm)
        $('span#accuracy').text(payload.score);
        $('span#test-samples').text(payload.n_test);
        $('span#train-samples').text(payload.n_train);
      
      });
    }
  });
  
})(jQuery);
