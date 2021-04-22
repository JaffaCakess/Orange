when HTTP_REQUEST {
    if { [HTTP::uri] starts_with "/" } then {
        HTTP::redirect http://task-6.example.com/demo-index.html
    }
    if { [HTTP::uri] starts_with "/test2" } then {
        HTTP::redirect http://task-6.example.com/demo-index.html
    }
}