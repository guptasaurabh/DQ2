/**
 * @author SESA249829
 */


$("#openup").click(function(){
	alert("helloboss")
	$.ajax({
	    type: 'GET',
	    url: 'testajax',
	    //dataType: 'json',
	     data: {
	         lastname: 'saurabh',
	        // firstname: $('#searchFirstName').val(),
	        // zipcode: $('#searchZipCode').val(),
	        // city: $('#searchCity').val()
	     },
	    success: function(data) {
	        alert("chal gaya")
	       	$("#adddata").html(data)
	            },
	    error: function(request, status, error) {
	       alert("error hai gaya")
	        return false;
	    },
	    complete: function() {
	        //do something
	    }
	});
});

function getsubdepartment(n){
	$.ajax({
	    type: 'POST',
	    url: 'getsubdept',
	     data: {
	         id:$("#department_"+(n)).val(),
	         n:n
	     },
	    success: function(data) {
	       	$("#department_"+n).html(data)
	            },
	    error: function(request, status, error) {
	       alert("error hai gaya")
	        return false;
	    },
	    complete: function() {
	        //do something
	    }
	});

}

function getsubsubdepartment(n,m){
    $.ajax({
        type: 'POST',
        url: 'getsubdept',
         data: {
             id:$("#department_"+(n)+(m)).val(),
             n:n,
             m:m
         },
        success: function(data) {
            $("#subdepartment_"+n+m).html(data)
                },
        error: function(request, status, error) {
           alert("error hai gaya")
            return false;
        },
        complete: function() {
            //do something
        }
    });

}
$("#department_base").change(function(){
	$.ajax({
	    type: 'GET',
	    url: 'testajax',
	    //dataType: 'json',
	     data: {
	         id:$("#department_base").val(),
	        // firstname: $('#searchFirstName').val(),
	        // zipcode: $('#searchZipCode').val(),
	        // city: $('#searchCity').val()
	     },
	    success: function(data) {
	       	$("#subdept_1").html(data)
	            },
	    error: function(request, status, error) {
	       alert("error hai gaya")
	        return false;
	    },
	    complete: function() {
	        //do something
	    }
	});
});
