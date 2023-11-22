dict_validate = {
    "add_pg" : {
        "check" : None,
        "module": "dialog",
        "function":"add_pages",
    },
    "delete_pg" : {
        "check" : "select_items_listWidget",
        "module": "edit_file",
        "function":"delete_selected_page",
    },
    "listWidget" : {
        "check" : None,
        "module": "display",
        "function":{
            "display_image",
            "on_dropped",
        },
    },
    "next_pg" : {
        "check" : None,
        "module": "display",
        "function":"next_page",
    },
    "back_pg" : {
        "check" : None,
        "module": "display",
        "function":"back_page",
    },
    "n_pg_edit" : {
        "check" : None,
        "module": "display",
        "function":"go_to_page",
    },
    "up_pg" : {
        "check" : None,
        "module": "display",
        "function":"move_page_up",
    },
    "down_pg" : {
        "check" : None,
        "module": "display",
        "function":"move_page_down",
    },
    "save_file" : {
        "check" : "count_row_listWidget",
        "module": "dialog",
        "function":"save_file",
    },
    "close_file" : {
        "check" : "count_row_listWidget",
        "module": "dialog",
        "function":"close_file",
    },
    "rotate_rigth" : {
        "check" : "select_items_listWidget",
        "module": "edit_file",
        "function":"rotate_image_r",
    },
    "rotate_left" : {
        "check" : "select_items_listWidget",
        "module": "edit_file",
        "function":"rotate_image_l",
    },
    "zoom_in" : {
        "check" : "select_items_listWidget",
        "module": "display",
        "function":"zoom_in",
    },
    "zoom_out" : {
        "check" : "select_items_listWidget",
        "module": "display",
        "function":"zoom_out",
    },
    "horizontalSlider" : {
        "check" : "select_items_listWidget",
        "module": "display",
        "function":"zoom_slider_changed",
    },
    "to_divide_file" : {
        "check" : "count_row_listWidget",
        "module": "dialog",
        "function":"zoom_slider_changed",
    },
    "zip_file" : {
        "check" : "count_row_listWidget",
        "module": "zip_file",
        "function":"zip_file",
    },
    "add_new_file" : {
        "check" : None,
        "module": "dialog",
        "function":"add_pages",
    },
    "add_m_d_agua" : {
        "check" : "count_row_listWidget",
        "module": "marca_dagua",
        "function":"add_watermark",
    },

    
}