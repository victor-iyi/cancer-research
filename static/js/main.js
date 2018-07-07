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

      name: $('input[name="name"]').val(),
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
      data = data.data;

      var $label = $('#cancer-result');

      $label.text(data.prediction);
      $('#patient-name').text(data.name);

      // use appropriate class label
      if (data.prediction.toString().toLowerCase() === 'benign') {
        $label.addClass('label-success');
      } else {
        $label.addClass('label-danger');
      }

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
    
    var algorithm = $('select#algorithm').val();
    var mode = $('select#mode').val();
    if (algorithm === '' || mode == '') {
      $('.form-error').show();
      
      $("p.error").text("All fields are required!");
    } else {
      // Everything went well...
      $.getJSON('/_settings', { algorithm: algorithm, mode: mode }, function (data) {
        data = data.data;

        // Display error.
        if (data.error !== null)
          return $('p.error').text(data.error);
        
        // Update views.
        $('span#algorithm').text(data.algorithm)
        $('span#accuracy').text(data.score);
        $('span#test-samples').text(data.n_test);
        $('span#train-samples').text(data.n_train);
      
      });
    }
  });
  
})(jQuery);
