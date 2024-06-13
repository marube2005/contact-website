import { useState , useEffect} from 'react'
import ContactList from './ContactList'
import './App.css'
import ContactForm from './ContactForm'

function App() {                                //function to try and fetch the contacts from our backend.
  const [contacts, setContacts] = useState([])

  useEffect(() => {
    fetchContacts()
 }, [] )

  const fetchContacts = async (req, res) => {
    const response = await fetch("http://127.0.0.1:5000/contacts")
    const data = await response.json()
    setContacts(data.contacts)
    console.log(data.contacts)
  }
  return <><ContactList contacts={contacts}/>
   <ContactForm/>
   </>
}
export default App
