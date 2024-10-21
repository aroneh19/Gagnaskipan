from sortedcontainers import SortedDict

class Contact:
    def __init__(self, name, phone, email) -> None:
        self.name = name
        self.phone = phone
        self.email = email
    
class ContactList:
    def __init__(self):
        self.contact_map = {}
        self.name_map = SortedDict()
        self.phone_map = {}
        self.email_map = {}
        self.id_counter = 1 
        
    
    def add_contact(self, name, phone, email):
        unique_id = self.id_counter
        self.id_counter += 1
        
        new_contact = Contact(name, phone, email)

        self.contact_map[unique_id] = new_contact

        self.name_map[name] = unique_id
        self.phone_map[phone] = unique_id
        self.email_map[email] = unique_id

    def get_by_name(self, name):
        id = self.name_map.get(name)
        if id:
            return self.contact_map.get(id)
    
    def get_by_phone(self, phone):
        id = self.phone_map.get(phone)
        if id:
            return self.contact_map.get(id)

    def get_by_email(self, email):
        id = self.email_map.get(email)
        if id:
            return self.contact_map.get(id)

    def remove(self, id):
        contact = self.contact_map.get(id)
        if contact:
            del self.name_map[contact.name]
            del self.phone_map[contact.phone]
            del self.email_map[contact.email]
            del self.contact_map[id]

    def get_contacts_ordered_by_name(self):
        ordered_contacts = []
        for name in self.name_map:
            ordered_contacts.append(self.contact_map[self.name_map[name]])
        return ordered_contacts
        
    def __str__(self) -> str:
        result = ""
        for contact_id, contact in self.contact_map.items():
            result += f"ID: {contact_id}, Name: {contact.name}, Phone: {contact.phone}, Email: {contact.email}\n"
        return result
    
def test_contact_list():
    # Create a ContactList instance
    contact_list = ContactList()

    # Add contacts
    contact_list.add_contact("Aron", "1234567", "aron@example.com")
    contact_list.add_contact("Alice", "2345678", "alice@example.com")
    contact_list.add_contact("Bob", "3456789", "bob@example.com")

    # Test get_by_name
    assert contact_list.get_by_name("Aron").email == "aron@example.com"
    assert contact_list.get_by_name("Alice").phone == "2345678"
    assert contact_list.get_by_name("Charlie") is None  # Non-existent contact

    # Test get_by_phone
    assert contact_list.get_by_phone("1234567").name == "Aron"
    assert contact_list.get_by_phone("3456789").email == "bob@example.com"
    assert contact_list.get_by_phone("9999999") is None  # Non-existent contact

    # Test get_by_email
    assert contact_list.get_by_email("alice@example.com").name == "Alice"
    assert contact_list.get_by_email("unknown@example.com") is None  # Non-existent contact

    # Test remove
    contact_id_to_remove = contact_list.get_by_name("Aron").id
    contact_list.remove(contact_id_to_remove)
    assert contact_list.get_by_name("Aron") is None

    # Test get_contacts_ordered_by_name
    ordered_contacts = contact_list.get_contacts_ordered_by_name()
    assert ordered_contacts[0].name == "Alice"
    assert ordered_contacts[1].name == "Bob"
    assert len(ordered_contacts) == 2  # One contact was removed

    print("All tests passed successfully.")

if __name__ == "__main__":
    test_contact_list()