<script type="text/javascript">
    $(document).ready(function () {
        $("#ajax-text-me").click(function() {
            $.ajax({
                type: 'GET',
                async: true,
                url: '/ajax/',
                data: "param1=value1&param2=value2;",
                success: function(data) {
                    $("#more-text-here1").append(data['first-text']);
                    $("#more-text-here2").append(data['second-text']);

                },
                dataType: 'json',
            });
        });
    });
</script>