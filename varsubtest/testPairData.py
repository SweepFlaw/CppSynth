import os
import sys
import time

from solver import makeSolution
from setting import *


def findTC(contestStr, questionStr):
    basePath = TC_DIR
    contestTCPath = os.path.join(basePath, contestStr)
    questionTCPath = os.path.join(contestTCPath, questionStr)
    resultCode = 0
    if not os.path.isdir(questionTCPath):
        resultCode = 1
    elif len(next(os.walk(os.path.join(questionTCPath, 'input')))[2]) < 1:
        resultCode = 2
    return resultCode, questionTCPath


### OUTPUT:
# - result code (int) (0 - success, 1 - not found, 2 - timeout, 3 - no testcase, 4 - wafile error)
# - wrong code itself, string
# - modified code itself, string
# - original ok code itself, string
# - the size of vscm list, integer
# - which item is substituted (vscmIndex), integer list
# - running time, integer(second)
# - human solving time, integer(second)
# - running time, integer(second)
# - human solving time, integer(second)
# - running iteration count, integer
# - vscm Modifier's recommendation length, integer

def modifyOne(wacodeFname, okcodeFname, inputTCDir, outputTCDir):
    modified_src, modified_linNums, used_vscmIndices, return_status, result_codes, elapsed_time, valid_moditer_count, recommendation_length, vscm_length = makeSolution(
        wacodeFname,
        inputTCDir,
        outputTCDir
    )
    
    with open(okcodeFname, 'r') as okf:
        ok_src = okf.read()
    with open(wacodeFname, 'r') as waf:
        wa_src = waf.read()
        
    wacodeFnameBase = os.path.basename(wacodeFname)
    okcodeFnameBase = os.path.basename(okcodeFname)
    wacodeTime = int(wacodeFnameBase[:(-6)])
    okcodeTime = int(okcodeFnameBase[:(-6)])
    human_solving_time = okcodeTime - wacodeTime
    
    return return_status, wa_src, modified_src, ok_src, vscm_length, used_vscmIndices, modified_linNums, elapsed_time, human_solving_time, valid_moditer_count, recommendation_length



### PREPARE INGREDIENTS
pairDataDir = PROBLEM_DIR
pdDirnames = sorted(next(os.walk(pairDataDir))[1])[LOWER_CLOSED_415_LIMIT:UPPER_OPENED_415_LIMIT]
pdDirnamesBaseSplitted = [os.path.basename(x).split('_') for x in pdDirnames]
pdDirContestStr = [x[0] for x in pdDirnamesBaseSplitted]
pdDirQuestionStr = [x[1] for x in pdDirnamesBaseSplitted]

pdDirnamesFull = [os.path.join(pairDataDir, x) for x in pdDirnames]
pdFilenames = [next(os.walk(x))[2] for x in pdDirnamesFull]

pdOKFilenames = [list(filter(lambda k: 'OK' in k, x))[0] for x in pdFilenames]
pdWAFilenames = [list(filter(lambda k: 'WA' in k, x))[0] for x in pdFilenames]

pdOKFilenamesFull = [os.path.join(dnf, okf) for dnf, okf in zip(pdDirnamesFull, pdOKFilenames)]
pdWAFilenamesFull = [os.path.join(dnf, waf) for dnf, waf in zip(pdDirnamesFull, pdWAFilenames)]



def runAll():
    summary_fnames = []
    summary_return_status = []
    summary_human_solving_time = []
    summary_running_time = []
    summary_vscm_length = []
    summary_valid_moditer_count = []
    summary_recommendation_length = []
    
    runningStatusCount = 0
    startTime = time.time()
    return_status = -1
    valid_moditer_count = -1
    if DEBUG_PRINT:
        print('runAll : dbg: # of W/A codes: ', len(pdDirContestStr))
    for cnstr, qsstr, okfn, wafn in zip(pdDirContestStr, pdDirQuestionStr, pdOKFilenamesFull, pdWAFilenamesFull):
        if DEBUG_PRINT:
            print('\nrunAll : dbg: for-loop: loop #', str(runningStatusCount), ' in ', str(len(pdDirContestStr)))
            print('||  contest  : ', cnstr)
            print('||  question : ', qsstr)
            print('||  wrong-answer filename : ', wafn)
            print('||  ok-answer    filename : ', okfn)
            
        ftc_rc, qtc_path = findTC(cnstr, qsstr)
        contest_str = cnstr
        question_str = qsstr
        wa_fn = wafn
        ok_fn = okfn        
        
        if ftc_rc == 0:
            if DEBUG_PRINT:
                print('runAll : dbg: this W/A code has testcases.')
            return_status, wrong_src, modified_src, ok_src, vscm_length, used_vscmIndices, modified_linNums, running_time, human_solving_time, valid_moditer_count, recommendation_length = modifyOne(
                wafn,
                okfn,
                os.path.join(qtc_path, 'input'),
                os.path.join(qtc_path, 'output')
            )
        else:
            print('runAll : dbg: this W/A code has no testcases.')
            continue  
            
        if DEBUG_PRINT:
            print('runAll : dbg: Human Solving Time: ', human_solving_time)
            print('runAll : dbg: modifyOne FINISHED')
            
        sys.stdout.flush()
            
        # write output in loop
        fname = contest_str + '_' + question_str + '_modified_' + os.path.basename(wa_fn)
        fname_full = os.path.join(LOG_DIR, fname)
        with open(fname_full, 'w') as logfile:
            logfile.write('1. contest_str\t2. question_str\t3. wa_fn\t4. ok_fn\n')
            logfile.write('5. return_status\t6. vscm_length\t7. modified_linNums\t8. running_time\n')
            logfile.write('9. human_solving_time\t10. valid_moditer_count\t11. recommendation_length\n')
            logfile.write('12~14: wa, modified, ok src\n')
            logfile.write(contest_str + '\n')
            logfile.write(question_str + '\n')
            logfile.write(wa_fn + '\n')
            logfile.write(ok_fn + '\n')
            logfile.write(str(return_status) + '\n')
            logfile.write(str(vscm_length) + '\n')
            logfile.write(str(modified_linNums) + '\n')
            logfile.write(str(running_time) + '\n')
            logfile.write(str(human_solving_time) + '\n')
            logfile.write(str(valid_moditer_count) + '\n')
            logfile.write(str(recommendation_length) + '\n')
            logfile.write('\n' + wrong_src + '\n')
            logfile.write('\n' + modified_src + '\n')
            logfile.write('\n' + ok_src + '\n')
        
        summary_fnames.append(fname)
        summary_return_status.append(return_status)
        summary_human_solving_time.append(human_solving_time)
        summary_running_time.append(running_time)
        summary_vscm_length.append(vscm_length)
        summary_valid_moditer_count.append(valid_moditer_count)
        summary_recommendation_length.append(recommendation_length)
        
    # write summary
    if DEBUG_PRINT:
            print('runAll : dbg: runAll write-summary START')
    rs_0_count = 0
    hst_sum = 0
    rt_sum = 0
    vl_sum = 0
    vmc_sum = 0
    rl_sum = 0
    refined_summary_human_solving_time = [(HUMANTIME_UPPER_LIMIT if x > HUMANTIME_UPPER_LIMIT else x) for x in summary_human_solving_time]
    for i, c in enumerate(summary_return_status):
        if c == 0:
            rs_0_count += 1
            hst_sum += refined_summary_human_solving_time[i]
            rt_sum += summary_running_time[i]
            vl_sum += summary_vscm_length[i]
            vmc_sum += summary_valid_moditer_count[i]
            rl_sum += summary_recommendation_length[i]
    
    with open(SUMMARY_LOGFILENAME, 'w') as logfile:
        logfile.write('<<<SUMMARY LOG>>>\n')
        logfile.write('<ReturnStatus-0-Case Summary>\n')
        if rs_0_count != 0:
            logfile.write('returnStatus_0_count: ' + str(rs_0_count) + '\n')
            logfile.write('refined_human_solving_time_avg: ' + str(hst_sum / rs_0_count) + '\n')
            logfile.write('running_time_avg: ' + str(rt_sum / rs_0_count) + '\n')
            logfile.write('vscm_length_avg: ' + str(vl_sum / rs_0_count) + '\n')
            logfile.write('iterCount_avg: ' + str(vmc_sum / rs_0_count) + '\n')
            logfile.write('recommendation_length: ' + str(rl_sum / rs_0_count) + '\n')
        else:
            logfile.write('returnStatus_0_count is ZERO\n')
        
        logfile.write('<General Summary>\n')
        logfile.write('test_performed_count: ' + str(len(summary_return_status)) + '\n')
        logfile.write('refined_human_solving_time_sum: ' + str(sum(refined_summary_human_solving_time)) + '\n')
        logfile.write('running_time_sum: ' + str(sum(summary_running_time)) + '\n')
        logfile.write('vscm_length_sum: ' + str(sum(summary_vscm_length)) + '\n')
        logfile.write('iterCount_sum: ' + str(sum(summary_valid_moditer_count)) + '\n')
        logfile.write('recommendation_length_sum: ' + str(sum(summary_recommendation_length)) + '\n')
        
        logfile.write('\n<<<DETAIL LOG>>>\n')
        logfile.write('\nLOG_FILE_NAMES\n')
        logfile.write(str(summary_fnames))
        logfile.write('\nRETURN STATUS\n')
        logfile.write(str(summary_return_status))
        logfile.write('\nUNREFINED_HUMAN_SOLVING_TIMES\n')
        logfile.write(str(summary_human_solving_time))
        logfile.write('\nRUNNING_TIMES\n')
        logfile.write(str(summary_running_time))
        logfile.write('\nVSCM_LENGTH\n')
        logfile.write(str(summary_vscm_length))
        logfile.write('\nVALID_MODITER_COUNT\n')
        logfile.write(str(summary_valid_moditer_count))
        logfile.write('\nRECOMMENDATION_LENGTH\n')
        logfile.write(str(summary_recommendation_length))
        logfile.write('\n')
    
    if DEBUG_PRINT:
            print('runAll : dbg: runAll write-summary FINISHED')
            print('runAll : dbg: runAll FINISHED')

if __name__ == '__main__':
    runAll()