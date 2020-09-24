// funciones para hacer los cálculos en la nómina

function calcular_nomina() {

    var nombre_parafiscal,nombre_extras, valpagar, valpagar2, parafiscal,subtotal,total,cant_horas,horas_extras;
    
    nombre_parafiscal=$("#id_nombre_parafiscal").val();
    nombre_extras=$("#id_nombre_extras").val();
  
   
    parafiscal=$("#id_parafiscales").val();
    
    
    cant_horas=$("#id_cantidad_horas").val();
    cant_horas = parseFloat(cant_horas)
    
    horas_extras=$("#id_horas").val();
    horas_extras = (parseInt(horas_extras)/100);
    

    valpagar=$("#id_valorpagar").val();
    valpagar = parseInt(valpagar)
    
    subtotal= (valpagar/240)*(horas_extras*(parseInt(cant_horas)))+valpagar;
    
    parafiscal  = (parseInt(parafiscal)/100) * valpagar;
  
    
    total= Math.round(subtotal - parafiscal) ;
    subtotal= Math.round(parseFloat(subtotal));
    total = parseFloat(total);
    valpagar = parseFloat(valpagar);
    valpagar2= parseFloat(document.getElementById("id_valorpagar2").value);
    
    $('#id_nombre_extras').val(nombre_extras);
    $('#id_parafiscales').val(parafiscal);
    $('#id_nombre_parafiscal').val(nombre_parafiscal);
    $('#id_subtotal').val(subtotal);
    $('#id_cantidad_horas').val(cant_horas);
    $('#id_horas').val(horas_extras);
    
    $('#id_valorpagar2').val(valpagar);
    $('#id_total').val(total);
    
    alert("Salario = $"+valpagar);
    
    
   // alert(id_nomina);
   // alert(horas_extras);

} 