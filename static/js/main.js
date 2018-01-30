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

  $('#classification-form').on('submit', function (e) {
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
      var $label = $('#cancer-result');
      var $header = $('.modal-header');

      var result = data.data.result.prediction;
      var name = data.data.name;
      $label.text(result);
      $header.text(name);
      // use appropriate class label
      if (result === 'benign') {
        $label.addClass('label-success');
      } else {
        $label.addClass('label-danger');
      }

      $('#myModal').modal('show');
    });
  });

})(jQuery);
