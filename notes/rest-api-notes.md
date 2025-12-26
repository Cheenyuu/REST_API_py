# REST API NOTES
Representational State Transfer Application Programming Interface

## Notes from here down are from this video:
- https://www.youtube.com/watch?v=qbLc5a9jdXo [REST API CRASH COURSE - Introduction + Full Python API Tutorial by Caleb Curry]

---

### API - Application Programming Interace
A way to say how two pieces of software communicate with each other.
Different applications that might be built differently will still be able to communicate with each other. You can build functionality separately while maintaining communication and information transfer.

Information is transferred one-way typically with a server-client relationship. Someone is serving up information when a request is sent. This is true for all API, however REST API has an important distinction: Instead of HTML the information is transferred by JSON.

    - JSON is a notation that describes information. (Javascript Object Notation | But not defined by JS, can be supported by any language and is now the standard for industry API)
    - JSON is just key-value pairs, like a dict in python or an object in JS.

### Client-Server Connection
'REST' describes the way in which the two programs are communicating with each other. It describes how information is transferred through the web, however instead of using HTML it uses JSON (as described earlier).

Furthermore, when a client-server connection is established through a REST API, endpoints are created a designated depending on the scope of information a client is allowed to get.

The connection endpoints and the information behind those endpoints follows the syntax of a URL.

    - DN or IP/id/id/... 
    - Continued to however many ids you may use to specify what information you want to get.

How you can define this actually is more freeform, however there are standards that are more widely used and understood.

    - api.DN or IP/id/...

### Why not connect a client directly to a database?
Generally speaking, it's not advisable because security problems. If someone were to directly access a server, they have no limit to the kind of information they are able to access.

### Interoperability
In the video Caleb goes over the reasons why this kind of system, the kind where you have a client that connects to a server and the server connects to the database, is effective. 
The main argument is that it's easy to make changes to that will be applicable to many different products or devices, having a middleman that isn't explicitly seen allows for modifications to be made discretely.
Interoperability just describes the ability of your API to be accessed an how it exchanges information. (https://www.ibm.com/think/topics/interoperability)



