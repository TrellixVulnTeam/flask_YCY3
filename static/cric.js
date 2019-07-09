$(function() {
    


 
    $('#match').click(function() {
        
      
        $.ajax({
            url : '/api/match' ,
            success: function(data) {
                $('#team').html(data['team'] );
                  $('#score').html(data['score'] );
                   $('#batsman').html(data['batsman'] );
                $('#run').html(data['run']);
                $('#wickets').html(data['wickets']);
                $('#overs').html(data['overs'] );
                 $('#time').html(data['time'] );
            }


        });


    });


})


