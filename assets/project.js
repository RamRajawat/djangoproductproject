$(document).ready(function(){
    $.getJSON('/fetchallproducttypes',function(data){
    data.map((item)=>{
    
        $('#producttype').append($('<option>').text(item.producttype).val(item.producttypeid))
    })
    })
    
    $('#producttype').change(function(){
    
        $.getJSON('/fetchallproductitems',{"producttypeid":$('#producttype').val()},function(data){
          
            $('#productitem').empty()
            $('#productitem').append($('<option>').text("-Select Product-"))
            data.map((item)=>{
            
                $('#productitem').append($('<option>').text(item.productitem).val(item.productitemid))
            })
            })
               
    
    })
    })