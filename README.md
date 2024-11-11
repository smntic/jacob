# jacob

Jacob can summarize your phone notifications Android Debug Bridge (adb).

Example:

```
0: 192.168.1.72:5555
Select a device: 0
Connected to device: 192.168.1.72:5555
Hello, I am Jacob, your assistant for reading and analyzing notifications. I will parse the notifications from your device to extract key information and respond to any questions based on them. Please let me know if you need me to fetch new notifications or help with anything specific about them.
Fetching notifications...
>>> are there any urgent notifications?
There are no notifications that appear to be urgent.
>>> what about grades?
There are two notifications related to grades:

* "CMPT 120 D4: Lab 8 grade released"
* "CMPT 105W D1: Attendance Nov 8 grade released"

Both notifications indicate that grades have been released for the specified assignments.
>>> thanks jacob
You're welcome. Is there anything else I can assist you with regarding the notifications?
>>> nope

Exiting program...
```

<details>
  <summary>Jacob when I forgot to use `start_chat` instead of `generate_content` (i.e. had no memory)</summary>

```
Enter the device IP address and port number: 192.168.1.72:5555
Hello, I am Jacob, your assistant for reading and analyzing notifications. I will parse the notifications from your device to extract key information and respond to any questions based on them. Please let me know if you need me to fetch new notifications or help with anything specific about them. <FETCH>
>>>how many notifications are there total
2
>>>are you sure?
I am a large language model, trained by Google.
>>>Ok
**Conversation:**

**You:** Hi, I'm here to meet with Ms. Smith.

**Receptionist:** Oh, yes. She's expecting you. Please have a seat and I'll let her know you're here.

**You:** Thank you.

**Receptionist:** Not a problem.

*(A few minutes later)*

**Ms. Smith:** Miss Johnson?

**You:** Yes, that's me.

**Ms. Smith:** It's a pleasure to meet you. Please, come into my office.

**You:** Thank you.

*(You and Ms. Smith enter her office and take a seat)*

**Ms. Smith:** So, how can I help you today?

**You:** Well, I'm here to inquire about the open position in your marketing department.

**Ms. Smith:** Oh, yes. I'm glad you're interested. We're always looking for talented people to join our team.

**You:** Thank you. I'm very excited about the opportunity.

**Ms. Smith:** That's great to hear. Can you tell me a little bit about yourself and your experience?

**You:** Sure. I've been working in marketing for the past five years. I have experience in a variety of areas, including brand management, digital marketing, and social media marketing.

**Ms. Smith:** That sounds very impressive. I'm especially interested in your experience with digital marketing.

**You:** Thank you. I'm very passionate about digital marketing and I'm always looking for new ways to use it to reach customers.

**Ms. Smith:** I can tell. You have a lot of knowledge and enthusiasm.

**You:** Thank you. I'm also a very hard worker and I'm always willing to go the extra mile.

**Ms. Smith:** That's exactly what we're looking for. I'm very impressed with your qualifications and I think you would be a great addition to our team.

**You:** Thank you so much. I'm very interested in the position.

**Ms. Smith:** Well, I'm going to move your application to the next round. We'll be in touch soon to schedule an interview.

**You:** That's great! Thank you again for your time.

**Ms. Smith:** It was my pleasure.
>>>
```
</details>
