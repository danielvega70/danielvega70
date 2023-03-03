using System.Collections;
using System.Collections.Generic;
using System.Reflection;
using UnityEngine;
using UnityEngine.Events;
//using SubjectNerd.Utilities;

public class EventListener : MonoBehaviour
{
    //[Reorderable]
    public List<EventAndResponse> eventAndResponses = new List<EventAndResponse>();

    private void OnEnable()
    {

        if (eventAndResponses.Count >= 1)
        {
            foreach (EventAndResponse eAndR in eventAndResponses)
            {
                eAndR.gameEvent.Register(this);
            }
        }


    }
    private void OnDisable()
    {
        if (eventAndResponses.Count >= 1)
        {
            foreach (EventAndResponse eAndR in eventAndResponses)
            {
                eAndR.gameEvent.DeRegister(this);
            }
        }
    }

    [ContextMenu("Raise Events")]
    public void OnEventRaised(GameEvent passedEvent)
    {

        for (int i = eventAndResponses.Count - 1; i >= 0; i--)
        {
            // Check if the passed event is the correct one
            if (passedEvent == eventAndResponses[i].gameEvent)
            {
                // Uncomment the line below for debugging the event listens and other details
                //Debug.Log("Called Event named: " + eventAndResponses[i].name + " on GameObject: " + gameObject.name);


                eventAndResponses[i].EventRaised();
            }
        }

    }
}


[System.Serializable]
public class EventAndResponse
{
    public string name;
    public GameEvent gameEvent;
    public UnityEvent response;
    public ResponseWithString responseForSentString;
    public ResponseWithInt responseForSentInt;
    public ResponseWithFloat responseForSentFloat;
    public ResponseWithBool responseForSentBool;

    public void EventRaised()
    {
        // default/generic
        if (response.GetPersistentEventCount() >= 1) // always check if at least 1 object is listening for the event
        {
            response.Invoke();
        }

        // string
        if (responseForSentString.GetPersistentEventCount() >= 1)
        {
            responseForSentString.Invoke(gameEvent.sentString);
        }

        // int
        if (responseForSentInt.GetPersistentEventCount() >= 1)
        {
            responseForSentInt.Invoke(gameEvent.sentInt);
        }

        // float
        if (responseForSentFloat.GetPersistentEventCount() >= 1)
        {
            responseForSentFloat.Invoke(gameEvent.sentFloat);
        }

        // bool
        if (responseForSentBool.GetPersistentEventCount() >= 1)
        {
            responseForSentBool.Invoke(gameEvent.sentBool);
        }

    }
}

[System.Serializable]
public class ResponseWithString : UnityEvent<string>
{
}

[System.Serializable]
public class ResponseWithInt : UnityEvent<int>
{
}

[System.Serializable]
public class ResponseWithFloat : UnityEvent<float>
{
}

[System.Serializable]
public class ResponseWithBool : UnityEvent<bool>
{
}
create a new script called GameEvent.cs and paste the following code into it::
using Trigger collider = new Trigger collider();
// if (SDL_PollEvent(&event))
// {
    // switch (event.type)
    // {
        // case SDL_QUIT:
            // mIsRunning = false;
            // break;
    // }
    put the collider into the game object 
    // const uint8_t* state = SDL_GetKeyboardState(NULL);
    // if (state[SDL_SCANCODE_ESCAPE])
    // {
        // mIsRunning = false;
    // }
    debug the game if it is working or not 
    private void Update()
    {
        // Update paddle direction based on W/S keys
        mPaddleDir = 0;
        if (Input.GetKey(KeyCode.W))
        {
            mPaddleDir -= 1;
        }
        if (Input.GetKey(KeyCode.S))
        {
            mPaddleDir += 1;
        }
    create game object for the character with mesh_render and box_collider 
    // Move paddle
        mPaddlePos.y += mPaddleDir * mPaddleSpeed * deltaTime;
        // Clamp paddle position within screen
        if (mPaddlePos.y < mPaddleH)
        {
            mPaddlePos.y = mPaddleH;
        }
        else if (mPaddlePos.y > (768.0f - mPaddleH))
        {
            mPaddlePos.y = 768.0f - mPaddleH;
        }
        mPaddlePos.x = 10.0f - mPaddleW;
        mPaddle->SetPosition(mPaddlePos);
