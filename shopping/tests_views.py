from django.test import TestCase
import pytest
from django.urls import reverse
from shopping.models import ShoppingList
from shopping. views import add_item, delete, edit_item
# Create your tests here.



@pytest.mark.django_db
def test_add_item(client):
    url = reverse('add_item')
    data = {'item_name': 'New Item'}
    response = client.post(url, data)
    assert response.status_code == 200


@pytest.mark.django_db
def test_edit_item(client):
    # Create a ShoppingList instance to edit
    shopping_list = ShoppingList.objects.create(item_name="Item to edit")

    # Get the URL for the edit view
    url = reverse('edit_item', args=[shopping_list.pk])

    # Prepare the data for editing
    new_item_name = "Updated Item"
    data = {'item_name': new_item_name}

    # Perform a POST request to edit the item
    response = client.post(url, data)

    # Assert the response status code
    assert response.status_code == 200

    # Verify that the item has been updated in the database
    updated_item = ShoppingList.objects.get(pk=shopping_list.pk)
    assert updated_item.item_name == new_item_name

@pytest.mark.django_db
def test_delete_item(client):
    # Create a ShoppingList instance to delete
    shopping_list = ShoppingList.objects.create(item_name="Item to delete")

    # Get the URL for the delete view
    url = reverse('delete', args=[shopping_list.pk])

    # Perform a POST request to delete the item
    response = client.post(url)

    # Assert the response status code
    assert response.status_code == 200

    # Verify that the item has been deleted from the database
    with pytest.raises(ShoppingList.DoesNotExist):
        ShoppingList.objects.get(pk=shopping_list.pk)


