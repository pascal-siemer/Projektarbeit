function throwErrorIf(condition, message) {
    
    if (!condition) {
        return;
    }

    throw new Error(message);
}

function logObject(event, logMessage) {

    let message = '<<logging_Object>>';

    if(message != undefined) {
        message += `:: ${logMessage}`;
    }

    console.log(message);
    console.log(event);
    console.log('<<end_of_log>>');
}

function logError(event, logMessage) {

    let message = '<<logging_Object>>';

    if(message != undefined) {
        message += `:: ${logMessage}`;
    }

    console.error(message);
    console.error(event);
    console.error('<<end_of_log>>');
}