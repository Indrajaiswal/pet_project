$(document).ready(function(){
    $(".invisible-content").hide();
    $(document).on('click',"#btn",function(){
        var MoreLessButton=$(".invisible-content").is(":visible")?'Read More':'Read Less';
        $(this).text(MoreLessButton); 
        $(this).parent(".box").find(".invisible-content").toggle();  
        $(this).parent(".box").find(".visible-content").toggle();  
    });
});
