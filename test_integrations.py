def test_recommended_directions(
    authorized_client: Client,
    random_child_courses: alchemy.TestUserCourses,
) -> None:
    courses = authorized_client.get_courses_info()
    recommended_directions = courses.children[0].recommended_directions

    assert len(recommended_directions) == 7
    assert recommended_directions[0]["direction_name"] == "Все направления"
    assert recommended_directions[1]["direction_name"] == "Дизайн"
    assert recommended_directions[2]["direction_name"] == "Техномейкерство"
    assert (
        recommended_directions[3]["direction_name"]
        == "Программирование и Game Dev"
    )
    assert recommended_directions[4]["direction_name"] == "Авиамодели_БПЛА"
    assert recommended_directions[5]["direction_name"] == "Экспресс-курсы"
    assert (
        recommended_directions[6]["direction_name"]
        == "Спортивная робототехника"
    )
def test_callback_request(
    *,
    authorized_client: Client,
) -> None:
    # success
    success_data = {
        "username_name": "test_username_name",
    }
    response = authorized_client.post_callback_request(success_data)
    assert response.status_code == 200

    # invalid data
    invalid_data: Dict[str, Any] = {}
    response = authorized_client.post_callback_request(invalid_data)
    assert response.status_code == 200

    # invalid method
    response = authorized_client.get_callback_request()
    assert response.status_code == 405