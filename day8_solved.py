registers = dict()
highest = 0 
def inc(a, b): 
    registers[a] += b 
def dec(a, b): 
    registers[a] -= b 
def do_nothing():
    pass
if 'g' not in registers.keys(): registers['g'] = 0 
if 'bfx' not in registers.keys(): registers['bfx'] = 0 
dec('g', 231) if registers['bfx'] > -10 else do_nothing()
if registers['g'] > highest:
   highest = registers['g'] 
if 'k' not in registers.keys(): registers['k'] = 0 
if 'wfk' not in registers.keys(): registers['wfk'] = 0 
dec('k', -567) if registers['wfk'] == 0 else do_nothing()
if registers['k'] > highest:
   highest = registers['k'] 
if 'jq' not in registers.keys(): registers['jq'] = 0 
if 'a' not in registers.keys(): registers['a'] = 0 
inc('jq', 880) if registers['a'] < 2 else do_nothing()
if registers['jq'] > highest:
   highest = registers['jq'] 
if 'sh' not in registers.keys(): registers['sh'] = 0 
if 'nkr' not in registers.keys(): registers['nkr'] = 0 
inc('sh', -828) if registers['nkr'] < -5 else do_nothing()
if registers['sh'] > highest:
   highest = registers['sh'] 
if 'w' not in registers.keys(): registers['w'] = 0 
if 'nkr' not in registers.keys(): registers['nkr'] = 0 
inc('w', 595) if registers['nkr'] > -10 else do_nothing()
if registers['w'] > highest:
   highest = registers['w'] 
if 't' not in registers.keys(): registers['t'] = 0 
if 'bfx' not in registers.keys(): registers['bfx'] = 0 
dec('t', 737) if registers['bfx'] < 5 else do_nothing()
if registers['t'] > highest:
   highest = registers['t'] 
if 'ghj' not in registers.keys(): registers['ghj'] = 0 
if 'pr' not in registers.keys(): registers['pr'] = 0 
dec('ghj', -693) if registers['pr'] == 0 else do_nothing()
if registers['ghj'] > highest:
   highest = registers['ghj'] 
if 'yo' not in registers.keys(): registers['yo'] = 0 
if 't' not in registers.keys(): registers['t'] = 0 
inc('yo', -362) if registers['t'] == -741 else do_nothing()
if registers['yo'] > highest:
   highest = registers['yo'] 
if 'pr' not in registers.keys(): registers['pr'] = 0 
if 'g' not in registers.keys(): registers['g'] = 0 
inc('pr', -851) if registers['g'] <= -228 else do_nothing()
if registers['pr'] > highest:
   highest = registers['pr'] 
if 'lpi' not in registers.keys(): registers['lpi'] = 0 
if 'lpi' not in registers.keys(): registers['lpi'] = 0 
inc('lpi', 628) if registers['lpi'] <= 0 else do_nothing()
if registers['lpi'] > highest:
   highest = registers['lpi'] 
if 'pr' not in registers.keys(): registers['pr'] = 0 
if 'qn' not in registers.keys(): registers['qn'] = 0 
inc('pr', -748) if registers['qn'] > -9 else do_nothing()
if registers['pr'] > highest:
   highest = registers['pr'] 
if 'rlq' not in registers.keys(): registers['rlq'] = 0 
if 'k' not in registers.keys(): registers['k'] = 0 
dec('rlq', -290) if registers['k'] <= 574 else do_nothing()
if registers['rlq'] > highest:
   highest = registers['rlq'] 
if 'lpi' not in registers.keys(): registers['lpi'] = 0 
if 'wfk' not in registers.keys(): registers['wfk'] = 0 
inc('lpi', 252) if registers['wfk'] == -4 else do_nothing()
if registers['lpi'] > highest:
   highest = registers['lpi'] 
if 'nkr' not in registers.keys(): registers['nkr'] = 0 
if 'bfx' not in registers.keys(): registers['bfx'] = 0 
dec('nkr', -674) if registers['bfx'] >= -7 else do_nothing()
if registers['nkr'] > highest:
   highest = registers['nkr'] 
if 'vh' not in registers.keys(): registers['vh'] = 0 
if 'fkp' not in registers.keys(): registers['fkp'] = 0 
dec('vh', 429) if registers['fkp'] != 6 else do_nothing()
if registers['vh'] > highest:
   highest = registers['vh'] 
if 'w' not in registers.keys(): registers['w'] = 0 
if 'w' not in registers.keys(): registers['w'] = 0 
dec('w', 568) if registers['w'] <= 604 else do_nothing()
if registers['w'] > highest:
   highest = registers['w'] 
if 'g' not in registers.keys(): registers['g'] = 0 
if 'vh' not in registers.keys(): registers['vh'] = 0 
dec('g', -700) if registers['vh'] >= -438 else do_nothing()
if registers['g'] > highest:
   highest = registers['g'] 
if 'lpi' not in registers.keys(): registers['lpi'] = 0 
if 'lpi' not in registers.keys(): registers['lpi'] = 0 
dec('lpi', 356) if registers['lpi'] >= 623 else do_nothing()
if registers['lpi'] > highest:
   highest = registers['lpi'] 
if 'afu' not in registers.keys(): registers['afu'] = 0 
if 'qn' not in registers.keys(): registers['qn'] = 0 
inc('afu', -227) if registers['qn'] <= 6 else do_nothing()
if registers['afu'] > highest:
   highest = registers['afu'] 
if 'm' not in registers.keys(): registers['m'] = 0 
if 'jq' not in registers.keys(): registers['jq'] = 0 
dec('m', 329) if registers['jq'] != 883 else do_nothing()
if registers['m'] > highest:
   highest = registers['m'] 
if 'qrc' not in registers.keys(): registers['qrc'] = 0 
if 'sh' not in registers.keys(): registers['sh'] = 0 
dec('qrc', 683) if registers['sh'] != 2 else do_nothing()
if registers['qrc'] > highest:
   highest = registers['qrc'] 
if 'sh' not in registers.keys(): registers['sh'] = 0 
if 'qdq' not in registers.keys(): registers['qdq'] = 0 
dec('sh', -322) if registers['qdq'] <= -7 else do_nothing()
if registers['sh'] > highest:
   highest = registers['sh'] 
if 'fkp' not in registers.keys(): registers['fkp'] = 0 
if 'qdq' not in registers.keys(): registers['qdq'] = 0 
inc('fkp', 112) if registers['qdq'] >= 7 else do_nothing()
if registers['fkp'] > highest:
   highest = registers['fkp'] 
if 'bfx' not in registers.keys(): registers['bfx'] = 0 
if 'wfk' not in registers.keys(): registers['wfk'] = 0 
dec('bfx', -258) if registers['wfk'] >= -1 else do_nothing()
if registers['bfx'] > highest:
   highest = registers['bfx'] 
if 'nkr' not in registers.keys(): registers['nkr'] = 0 
if 'ev' not in registers.keys(): registers['ev'] = 0 
inc('nkr', -259) if registers['ev'] >= -1 else do_nothing()
if registers['nkr'] > highest:
   highest = registers['nkr'] 
if 'pr' not in registers.keys(): registers['pr'] = 0 
if 'ghj' not in registers.keys(): registers['ghj'] = 0 
dec('pr', -806) if registers['ghj'] == 693 else do_nothing()
if registers['pr'] > highest:
   highest = registers['pr'] 
if 'w' not in registers.keys(): registers['w'] = 0 
if 'nkr' not in registers.keys(): registers['nkr'] = 0 
inc('w', -717) if registers['nkr'] >= 412 else do_nothing()
if registers['w'] > highest:
   highest = registers['w'] 
if 'rlq' not in registers.keys(): registers['rlq'] = 0 
if 'w' not in registers.keys(): registers['w'] = 0 
inc('rlq', -755) if registers['w'] < -686 else do_nothing()
if registers['rlq'] > highest:
   highest = registers['rlq'] 
if 'afu' not in registers.keys(): registers['afu'] = 0 
if 'yo' not in registers.keys(): registers['yo'] = 0 
inc('afu', 514) if registers['yo'] <= 2 else do_nothing()
if registers['afu'] > highest:
   highest = registers['afu'] 
if 'a' not in registers.keys(): registers['a'] = 0 
if 'bfx' not in registers.keys(): registers['bfx'] = 0 
inc('a', 697) if registers['bfx'] <= 252 else do_nothing()
if registers['a'] > highest:
   highest = registers['a'] 
if 'qrc' not in registers.keys(): registers['qrc'] = 0 
if 'lpi' not in registers.keys(): registers['lpi'] = 0 
dec('qrc', -733) if registers['lpi'] > 278 else do_nothing()
if registers['qrc'] > highest:
   highest = registers['qrc'] 
if 'jq' not in registers.keys(): registers['jq'] = 0 
if 'ghj' not in registers.keys(): registers['ghj'] = 0 
inc('jq', 843) if registers['ghj'] != 692 else do_nothing()
if registers['jq'] > highest:
   highest = registers['jq'] 
if 'jh' not in registers.keys(): registers['jh'] = 0 
if 'u' not in registers.keys(): registers['u'] = 0 
inc('jh', -321) if registers['u'] <= 3 else do_nothing()
if registers['jh'] > highest:
   highest = registers['jh'] 
if 'afu' not in registers.keys(): registers['afu'] = 0 
if 'afu' not in registers.keys(): registers['afu'] = 0 
dec('afu', -86) if registers['afu'] == 287 else do_nothing()
if registers['afu'] > highest:
   highest = registers['afu'] 
if 'g' not in registers.keys(): registers['g'] = 0 
if 'w' not in registers.keys(): registers['w'] = 0 
inc('g', -374) if registers['w'] >= -694 else do_nothing()
if registers['g'] > highest:
   highest = registers['g'] 
if 'm' not in registers.keys(): registers['m'] = 0 
if 'k' not in registers.keys(): registers['k'] = 0 
inc('m', 681) if registers['k'] < 565 else do_nothing()
if registers['m'] > highest:
   highest = registers['m'] 
if 'ev' not in registers.keys(): registers['ev'] = 0 
if 'u' not in registers.keys(): registers['u'] = 0 
inc('ev', -75) if registers['u'] == 0 else do_nothing()
if registers['ev'] > highest:
   highest = registers['ev'] 
if 'w' not in registers.keys(): registers['w'] = 0 
if 'lpi' not in registers.keys(): registers['lpi'] = 0 
dec('w', 130) if registers['lpi'] < 277 else do_nothing()
if registers['w'] > highest:
   highest = registers['w'] 
if 'ev' not in registers.keys(): registers['ev'] = 0 
if 'vh' not in registers.keys(): registers['vh'] = 0 
dec('ev', 139) if registers['vh'] == -429 else do_nothing()
if registers['ev'] > highest:
   highest = registers['ev'] 
if 'm' not in registers.keys(): registers['m'] = 0 
if 'm' not in registers.keys(): registers['m'] = 0 
inc('m', -283) if registers['m'] >= -332 else do_nothing()
if registers['m'] > highest:
   highest = registers['m'] 
if 'fkp' not in registers.keys(): registers['fkp'] = 0 
if 'yo' not in registers.keys(): registers['yo'] = 0 
dec('fkp', -48) if registers['yo'] != -2 else do_nothing()
if registers['fkp'] > highest:
   highest = registers['fkp'] 
if 'g' not in registers.keys(): registers['g'] = 0 
if 't' not in registers.keys(): registers['t'] = 0 
dec('g', -272) if registers['t'] > -747 else do_nothing()
if registers['g'] > highest:
   highest = registers['g'] 
if 'wfk' not in registers.keys(): registers['wfk'] = 0 
if 'pr' not in registers.keys(): registers['pr'] = 0 
dec('wfk', 752) if registers['pr'] < -800 else do_nothing()
if registers['wfk'] > highest:
   highest = registers['wfk'] 
if 'bfx' not in registers.keys(): registers['bfx'] = 0 
if 'rlq' not in registers.keys(): registers['rlq'] = 0 
inc('bfx', -164) if registers['rlq'] != -467 else do_nothing()
if registers['bfx'] > highest:
   highest = registers['bfx'] 
if 'k' not in registers.keys(): registers['k'] = 0 
if 'k' not in registers.keys(): registers['k'] = 0 
dec('k', -470) if registers['k'] <= 566 else do_nothing()
if registers['k'] > highest:
   highest = registers['k'] 
if 'ghj' not in registers.keys(): registers['ghj'] = 0 
if 'k' not in registers.keys(): registers['k'] = 0 
dec('ghj', 221) if registers['k'] < 572 else do_nothing()
if registers['ghj'] > highest:
   highest = registers['ghj'] 
if 'g' not in registers.keys(): registers['g'] = 0 
if 'bfx' not in registers.keys(): registers['bfx'] = 0 
dec('g', 722) if registers['bfx'] > 93 else do_nothing()
if registers['g'] > highest:
   highest = registers['g'] 
if 'wfk' not in registers.keys(): registers['wfk'] = 0 
if 'qdq' not in registers.keys(): registers['qdq'] = 0 
dec('wfk', -256) if registers['qdq'] >= -7 else do_nothing()
if registers['wfk'] > highest:
   highest = registers['wfk'] 
if 't' not in registers.keys(): registers['t'] = 0 
if 'bfx' not in registers.keys(): registers['bfx'] = 0 
inc('t', 337) if registers['bfx'] > 99 else do_nothing()
if registers['t'] > highest:
   highest = registers['t'] 
if 'w' not in registers.keys(): registers['w'] = 0 
if 'fkp' not in registers.keys(): registers['fkp'] = 0 
inc('w', 134) if registers['fkp'] != 48 else do_nothing()
if registers['w'] > highest:
   highest = registers['w'] 
if 'nkr' not in registers.keys(): registers['nkr'] = 0 
if 'w' not in registers.keys(): registers['w'] = 0 
inc('nkr', -605) if registers['w'] <= -815 else do_nothing()
if registers['nkr'] > highest:
   highest = registers['nkr'] 
if 'wfk' not in registers.keys(): registers['wfk'] = 0 
if 'vh' not in registers.keys(): registers['vh'] = 0 
dec('wfk', -938) if registers['vh'] >= -438 else do_nothing()
if registers['wfk'] > highest:
   highest = registers['wfk'] 
if 'pr' not in registers.keys(): registers['pr'] = 0 
if 'wfk' not in registers.keys(): registers['wfk'] = 0 
dec('pr', -938) if registers['wfk'] < 1204 else do_nothing()
if registers['pr'] > highest:
   highest = registers['pr'] 
if 'qn' not in registers.keys(): registers['qn'] = 0 
if 'rlq' not in registers.keys(): registers['rlq'] = 0 
inc('qn', -372) if registers['rlq'] <= -459 else do_nothing()
if registers['qn'] > highest:
   highest = registers['qn'] 
if 'bfx' not in registers.keys(): registers['bfx'] = 0 
if 'g' not in registers.keys(): registers['g'] = 0 
dec('bfx', -38) if registers['g'] <= -348 else do_nothing()
if registers['bfx'] > highest:
   highest = registers['bfx'] 
if 'qn' not in registers.keys(): registers['qn'] = 0 
if 'fkp' not in registers.keys(): registers['fkp'] = 0 
inc('qn', 561) if registers['fkp'] != 49 else do_nothing()
if registers['qn'] > highest:
   highest = registers['qn'] 
if 'ghj' not in registers.keys(): registers['ghj'] = 0 
if 'rlq' not in registers.keys(): registers['rlq'] = 0 
dec('ghj', 555) if registers['rlq'] >= -466 else do_nothing()
if registers['ghj'] > highest:
   highest = registers['ghj'] 
if 'qdq' not in registers.keys(): registers['qdq'] = 0 
if 'yo' not in registers.keys(): registers['yo'] = 0 
dec('qdq', 78) if registers['yo'] == 0 else do_nothing()
if registers['qdq'] > highest:
   highest = registers['qdq'] 
if 'ev' not in registers.keys(): registers['ev'] = 0 
if 'vh' not in registers.keys(): registers['vh'] = 0 
inc('ev', -466) if registers['vh'] > -433 else do_nothing()
if registers['ev'] > highest:
   highest = registers['ev'] 
if 'w' not in registers.keys(): registers['w'] = 0 
if 'qdq' not in registers.keys(): registers['qdq'] = 0 
inc('w', -946) if registers['qdq'] >= -84 else do_nothing()
if registers['w'] > highest:
   highest = registers['w'] 
if 'w' not in registers.keys(): registers['w'] = 0 
if 'ghj' not in registers.keys(): registers['ghj'] = 0 
inc('w', 735) if registers['ghj'] < -74 else do_nothing()
if registers['w'] > highest:
   highest = registers['w'] 
if 'lpi' not in registers.keys(): registers['lpi'] = 0 
if 'afu' not in registers.keys(): registers['afu'] = 0 
dec('lpi', -616) if registers['afu'] == 380 else do_nothing()
if registers['lpi'] > highest:
   highest = registers['lpi'] 
if 'nkr' not in registers.keys(): registers['nkr'] = 0 
if 'qrc' not in registers.keys(): registers['qrc'] = 0 
dec('nkr', 259) if registers['qrc'] != -678 else do_nothing()
if registers['nkr'] > highest:
   highest = registers['nkr'] 
if 'sh' not in registers.keys(): registers['sh'] = 0 
if 'm' not in registers.keys(): registers['m'] = 0 
dec('sh', -406) if registers['m'] < -620 else do_nothing()
if registers['sh'] > highest:
   highest = registers['sh'] 
if 'jq' not in registers.keys(): registers['jq'] = 0 
if 'm' not in registers.keys(): registers['m'] = 0 
dec('jq', -449) if registers['m'] == -612 else do_nothing()
if registers['jq'] > highest:
   highest = registers['jq'] 
if 'ev' not in registers.keys(): registers['ev'] = 0 
if 'qrc' not in registers.keys(): registers['qrc'] = 0 
dec('ev', 990) if registers['qrc'] > -691 else do_nothing()
if registers['ev'] > highest:
   highest = registers['ev'] 
if 'g' not in registers.keys(): registers['g'] = 0 
if 'jh' not in registers.keys(): registers['jh'] = 0 
dec('g', -139) if registers['jh'] > -315 else do_nothing()
if registers['g'] > highest:
   highest = registers['g'] 
if 'w' not in registers.keys(): registers['w'] = 0 
if 'vh' not in registers.keys(): registers['vh'] = 0 
inc('w', 204) if registers['vh'] <= -424 else do_nothing()
if registers['w'] > highest:
   highest = registers['w'] 
if 'yo' not in registers.keys(): registers['yo'] = 0 
if 'jq' not in registers.keys(): registers['jq'] = 0 
dec('yo', -26) if registers['jq'] == 2181 else do_nothing()
if registers['yo'] > highest:
   highest = registers['yo'] 
if 'a' not in registers.keys(): registers['a'] = 0 
if 'qrc' not in registers.keys(): registers['qrc'] = 0 
dec('a', -528) if registers['qrc'] != -688 else do_nothing()
if registers['a'] > highest:
   highest = registers['a'] 
if 'nkr' not in registers.keys(): registers['nkr'] = 0 
if 'bfx' not in registers.keys(): registers['bfx'] = 0 
inc('nkr', -926) if registers['bfx'] > 128 else do_nothing()
if registers['nkr'] > highest:
   highest = registers['nkr'] 
if 'qdq' not in registers.keys(): registers['qdq'] = 0 
if 'w' not in registers.keys(): registers['w'] = 0 
inc('qdq', -241) if registers['w'] <= -822 else do_nothing()
if registers['qdq'] > highest:
   highest = registers['qdq'] 
if 'g' not in registers.keys(): registers['g'] = 0 
if 'wfk' not in registers.keys(): registers['wfk'] = 0 
inc('g', -111) if registers['wfk'] == 1194 else do_nothing()
if registers['g'] > highest:
   highest = registers['g'] 
if 'bfx' not in registers.keys(): registers['bfx'] = 0 
if 'qn' not in registers.keys(): registers['qn'] = 0 
inc('bfx', 282) if registers['qn'] < 199 else do_nothing()
if registers['bfx'] > highest:
   highest = registers['bfx'] 
if 'jq' not in registers.keys(): registers['jq'] = 0 
if 'wfk' not in registers.keys(): registers['wfk'] = 0 
inc('jq', 413) if registers['wfk'] == 1194 else do_nothing()
if registers['jq'] > highest:
   highest = registers['jq'] 
if 'fkp' not in registers.keys(): registers['fkp'] = 0 
if 'ev' not in registers.keys(): registers['ev'] = 0 
dec('fkp', -281) if registers['ev'] < -1660 else do_nothing()
if registers['fkp'] > highest:
   highest = registers['fkp'] 
if 'qrc' not in registers.keys(): registers['qrc'] = 0 
if 'qn' not in registers.keys(): registers['qn'] = 0 
inc('qrc', -596) if registers['qn'] != 199 else do_nothing()
if registers['qrc'] > highest:
   highest = registers['qrc'] 
if 'ev' not in registers.keys(): registers['ev'] = 0 
if 'ghj' not in registers.keys(): registers['ghj'] = 0 
inc('ev', 383) if registers['ghj'] != -74 else do_nothing()
if registers['ev'] > highest:
   highest = registers['ev'] 
if 'sh' not in registers.keys(): registers['sh'] = 0 
if 'yo' not in registers.keys(): registers['yo'] = 0 
inc('sh', -562) if registers['yo'] <= -6 else do_nothing()
if registers['sh'] > highest:
   highest = registers['sh'] 
if 'sh' not in registers.keys(): registers['sh'] = 0 
if 'wfk' not in registers.keys(): registers['wfk'] = 0 
inc('sh', 728) if registers['wfk'] <= 1196 else do_nothing()
if registers['sh'] > highest:
   highest = registers['sh'] 
if 'bfx' not in registers.keys(): registers['bfx'] = 0 
if 'vh' not in registers.keys(): registers['vh'] = 0 
dec('bfx', -360) if registers['vh'] < -423 else do_nothing()
if registers['bfx'] > highest:
   highest = registers['bfx'] 
if 'jq' not in registers.keys(): registers['jq'] = 0 
if 'qn' not in registers.keys(): registers['qn'] = 0 
inc('jq', -774) if registers['qn'] >= 195 else do_nothing()
if registers['jq'] > highest:
   highest = registers['jq'] 
if 'qn' not in registers.keys(): registers['qn'] = 0 
if 'ghj' not in registers.keys(): registers['ghj'] = 0 
dec('qn', -939) if registers['ghj'] == -87 else do_nothing()
if registers['qn'] > highest:
   highest = registers['qn'] 
if 'w' not in registers.keys(): registers['w'] = 0 
if 'ghj' not in registers.keys(): registers['ghj'] = 0 
dec('w', 952) if registers['ghj'] == -83 else do_nothing()
if registers['w'] > highest:
   highest = registers['w'] 
if 'yo' not in registers.keys(): registers['yo'] = 0 
if 'lpi' not in registers.keys(): registers['lpi'] = 0 
dec('yo', -112) if registers['lpi'] < 278 else do_nothing()
if registers['yo'] > highest:
   highest = registers['yo'] 
if 'qn' not in registers.keys(): registers['qn'] = 0 
if 'sh' not in registers.keys(): registers['sh'] = 0 
dec('qn', 902) if registers['sh'] == 728 else do_nothing()
if registers['qn'] > highest:
   highest = registers['qn'] 
if 'k' not in registers.keys(): registers['k'] = 0 
if 'qrc' not in registers.keys(): registers['qrc'] = 0 
dec('k', 507) if registers['qrc'] == -1279 else do_nothing()
if registers['k'] > highest:
   highest = registers['k'] 
if 'g' not in registers.keys(): registers['g'] = 0 
if 'a' not in registers.keys(): registers['a'] = 0 
dec('g', 155) if registers['a'] != 537 else do_nothing()
if registers['g'] > highest:
   highest = registers['g'] 
if 'rlq' not in registers.keys(): registers['rlq'] = 0 
if 'a' not in registers.keys(): registers['a'] = 0 
inc('rlq', 655) if registers['a'] < 530 else do_nothing()
if registers['rlq'] > highest:
   highest = registers['rlq'] 
if 'qrc' not in registers.keys(): registers['qrc'] = 0 
if 'afu' not in registers.keys(): registers['afu'] = 0 
inc('qrc', 523) if registers['afu'] == 373 else do_nothing()
if registers['qrc'] > highest:
   highest = registers['qrc'] 
if 't' not in registers.keys(): registers['t'] = 0 
if 'jh' not in registers.keys(): registers['jh'] = 0 
dec('t', 36) if registers['jh'] != -319 else do_nothing()
if registers['t'] > highest:
   highest = registers['t'] 
if 'qn' not in registers.keys(): registers['qn'] = 0 
if 'm' not in registers.keys(): registers['m'] = 0 
dec('qn', -584) if registers['m'] > -610 else do_nothing()
if registers['qn'] > highest:
   highest = registers['qn'] 
if 'ev' not in registers.keys(): registers['ev'] = 0 
if 'sh' not in registers.keys(): registers['sh'] = 0 
inc('ev', 406) if registers['sh'] <= 730 else do_nothing()
if registers['ev'] > highest:
   highest = registers['ev'] 
if 'pr' not in registers.keys(): registers['pr'] = 0 
if 'lpi' not in registers.keys(): registers['lpi'] = 0 
dec('pr', 699) if registers['lpi'] > 277 else do_nothing()
if registers['pr'] > highest:
   highest = registers['pr'] 
if 'a' not in registers.keys(): registers['a'] = 0 
if 'k' not in registers.keys(): registers['k'] = 0 
dec('a', 906) if registers['k'] == 60 else do_nothing()
if registers['a'] > highest:
   highest = registers['a'] 
if 'jq' not in registers.keys(): registers['jq'] = 0 
if 'm' not in registers.keys(): registers['m'] = 0 
dec('jq', -811) if registers['m'] != -615 else do_nothing()
if registers['jq'] > highest:
   highest = registers['jq'] 
if 'vh' not in registers.keys(): registers['vh'] = 0 
if 'qn' not in registers.keys(): registers['qn'] = 0 
inc('vh', -874) if registers['qn'] <= -712 else do_nothing()
if registers['vh'] > highest:
   highest = registers['vh'] 
if 'pr' not in registers.keys(): registers['pr'] = 0 
if 'vh' not in registers.keys(): registers['vh'] = 0 
inc('pr', 325) if registers['vh'] != -1293 else do_nothing()
if registers['pr'] > highest:
   highest = registers['pr'] 
if 'nkr' not in registers.keys(): registers['nkr'] = 0 
if 'm' not in registers.keys(): registers['m'] = 0 
inc('nkr', -786) if registers['m'] < -607 else do_nothing()
if registers['nkr'] > highest:
   highest = registers['nkr'] 
if 'pr' not in registers.keys(): registers['pr'] = 0 
if 'jq' not in registers.keys(): registers['jq'] = 0 
inc('pr', -903) if registers['jq'] != 3389 else do_nothing()
if registers['pr'] > highest:
   highest = registers['pr'] 
if 'fkp' not in registers.keys(): registers['fkp'] = 0 
if 'rlq' not in registers.keys(): registers['rlq'] = 0 
inc('fkp', 758) if registers['rlq'] <= 182 else do_nothing()
if registers['fkp'] > highest:
   highest = registers['fkp'] 
if 'lpi' not in registers.keys(): registers['lpi'] = 0 
if 'sh' not in registers.keys(): registers['sh'] = 0 
inc('lpi', -307) if registers['sh'] > 725 else do_nothing()
if registers['lpi'] > highest:
   highest = registers['lpi'] 
if 'afu' not in registers.keys(): registers['afu'] = 0 
if 'jh' not in registers.keys(): registers['jh'] = 0 
inc('afu', -162) if registers['jh'] <= -314 else do_nothing()
if registers['afu'] > highest:
   highest = registers['afu'] 
if 'afu' not in registers.keys(): registers['afu'] = 0 
if 'k' not in registers.keys(): registers['k'] = 0 
inc('afu', -96) if registers['k'] < 63 else do_nothing()
if registers['afu'] > highest:
   highest = registers['afu'] 
if 't' not in registers.keys(): registers['t'] = 0 
if 'pr' not in registers.keys(): registers['pr'] = 0 
dec('t', 939) if registers['pr'] <= -427 else do_nothing()
if registers['t'] > highest:
   highest = registers['t'] 
if 'fkp' not in registers.keys(): registers['fkp'] = 0 
if 'a' not in registers.keys(): registers['a'] = 0 
dec('fkp', -65) if registers['a'] <= -370 else do_nothing()
if registers['fkp'] > highest:
   highest = registers['fkp'] 
if 'g' not in registers.keys(): registers['g'] = 0 
if 'nkr' not in registers.keys(): registers['nkr'] = 0 
dec('g', 246) if registers['nkr'] > -2160 else do_nothing()
if registers['g'] > highest:
   highest = registers['g'] 
if 'w' not in registers.keys(): registers['w'] = 0 
if 'sh' not in registers.keys(): registers['sh'] = 0 
inc('w', 62) if registers['sh'] != 727 else do_nothing()
if registers['w'] > highest:
   highest = registers['w'] 
if 'jh' not in registers.keys(): registers['jh'] = 0 
if 'ev' not in registers.keys(): registers['ev'] = 0 
dec('jh', -621) if registers['ev'] > -891 else do_nothing()
if registers['jh'] > highest:
   highest = registers['jh'] 
if 'wfk' not in registers.keys(): registers['wfk'] = 0 
if 'ev' not in registers.keys(): registers['ev'] = 0 
dec('wfk', -84) if registers['ev'] != -878 else do_nothing()
if registers['wfk'] > highest:
   highest = registers['wfk'] 
if 'qdq' not in registers.keys(): registers['qdq'] = 0 
if 'sh' not in registers.keys(): registers['sh'] = 0 
inc('qdq', 245) if registers['sh'] > 725 else do_nothing()
if registers['qdq'] > highest:
   highest = registers['qdq'] 
if 'qdq' not in registers.keys(): registers['qdq'] = 0 
if 'jh' not in registers.keys(): registers['jh'] = 0 
dec('qdq', 689) if registers['jh'] < 310 else do_nothing()
if registers['qdq'] > highest:
   highest = registers['qdq'] 
if 'sh' not in registers.keys(): registers['sh'] = 0 
if 'ghj' not in registers.keys(): registers['ghj'] = 0 
inc('sh', -396) if registers['ghj'] < -79 else do_nothing()
if registers['sh'] > highest:
   highest = registers['sh'] 
if 'yo' not in registers.keys(): registers['yo'] = 0 
if 'pr' not in registers.keys(): registers['pr'] = 0 
dec('yo', 457) if registers['pr'] < -429 else do_nothing()
if registers['yo'] > highest:
   highest = registers['yo'] 
if 'vh' not in registers.keys(): registers['vh'] = 0 
if 'pr' not in registers.keys(): registers['pr'] = 0 
dec('vh', -545) if registers['pr'] > -434 else do_nothing()
if registers['vh'] > highest:
   highest = registers['vh'] 
if 'rlq' not in registers.keys(): registers['rlq'] = 0 
if 'nkr' not in registers.keys(): registers['nkr'] = 0 
inc('rlq', -848) if registers['nkr'] > -2166 else do_nothing()
if registers['rlq'] > highest:
   highest = registers['rlq'] 
if 'nkr' not in registers.keys(): registers['nkr'] = 0 
if 'fkp' not in registers.keys(): registers['fkp'] = 0 
inc('nkr', 274) if registers['fkp'] < 401 else do_nothing()
if registers['nkr'] > highest:
   highest = registers['nkr'] 
if 'nkr' not in registers.keys(): registers['nkr'] = 0 
if 'fkp' not in registers.keys(): registers['fkp'] = 0 
inc('nkr', -165) if registers['fkp'] > 393 else do_nothing()
if registers['nkr'] > highest:
   highest = registers['nkr'] 
if 'u' not in registers.keys(): registers['u'] = 0 
if 't' not in registers.keys(): registers['t'] = 0 
dec('u', 973) if registers['t'] <= -1706 else do_nothing()
if registers['u'] > highest:
   highest = registers['u'] 
if 'vh' not in registers.keys(): registers['vh'] = 0 
if 'wfk' not in registers.keys(): registers['wfk'] = 0 
dec('vh', -874) if registers['wfk'] < 1286 else do_nothing()
if registers['vh'] > highest:
   highest = registers['vh'] 
if 'ghj' not in registers.keys(): registers['ghj'] = 0 
if 'lpi' not in registers.keys(): registers['lpi'] = 0 
inc('ghj', 872) if registers['lpi'] == -35 else do_nothing()
if registers['ghj'] > highest:
   highest = registers['ghj'] 
if 'vh' not in registers.keys(): registers['vh'] = 0 
if 't' not in registers.keys(): registers['t'] = 0 
dec('vh', 476) if registers['t'] == -1712 else do_nothing()
if registers['vh'] > highest:
   highest = registers['vh'] 
if 'lpi' not in registers.keys(): registers['lpi'] = 0 
if 'nkr' not in registers.keys(): registers['nkr'] = 0 
inc('lpi', -780) if registers['nkr'] > -2062 else do_nothing()
if registers['lpi'] > highest:
   highest = registers['lpi'] 
if 'a' not in registers.keys(): registers['a'] = 0 
if 'sh' not in registers.keys(): registers['sh'] = 0 
inc('a', 312) if registers['sh'] != 332 else do_nothing()
if registers['a'] > highest:
   highest = registers['a'] 
if 'qdq' not in registers.keys(): registers['qdq'] = 0 
if 'a' not in registers.keys(): registers['a'] = 0 
dec('qdq', -840) if registers['a'] == -378 else do_nothing()
if registers['qdq'] > highest:
   highest = registers['qdq'] 
if 'k' not in registers.keys(): registers['k'] = 0 
if 'qn' not in registers.keys(): registers['qn'] = 0 
dec('k', 287) if registers['qn'] <= -707 else do_nothing()
if registers['k'] > highest:
   highest = registers['k'] 
if 'rlq' not in registers.keys(): registers['rlq'] = 0 
if 'jh' not in registers.keys(): registers['jh'] = 0 
dec('rlq', 250) if registers['jh'] != 304 else do_nothing()
if registers['rlq'] > highest:
   highest = registers['rlq'] 
if 'qdq' not in registers.keys(): registers['qdq'] = 0 
if 'qrc' not in registers.keys(): registers['qrc'] = 0 
dec('qdq', -870) if registers['qrc'] == -756 else do_nothing()
if registers['qdq'] > highest:
   highest = registers['qdq'] 
if 'pr' not in registers.keys(): registers['pr'] = 0 
if 'qrc' not in registers.keys(): registers['qrc'] = 0 
dec('pr', 95) if registers['qrc'] < -750 else do_nothing()
if registers['pr'] > highest:
   highest = registers['pr'] 
if 'm' not in registers.keys(): registers['m'] = 0 
if 'jq' not in registers.keys(): registers['jq'] = 0 
dec('m', 21) if registers['jq'] <= 3400 else do_nothing()
if registers['m'] > highest:
   highest = registers['m'] 
if 'qrc' not in registers.keys(): registers['qrc'] = 0 
if 'vh' not in registers.keys(): registers['vh'] = 0 
dec('qrc', -995) if registers['vh'] == -360 else do_nothing()
if registers['qrc'] > highest:
   highest = registers['qrc'] 
if 'fkp' not in registers.keys(): registers['fkp'] = 0 
if 'g' not in registers.keys(): registers['g'] = 0 
inc('fkp', 422) if registers['g'] > -626 else do_nothing()
if registers['fkp'] > highest:
   highest = registers['fkp'] 
if 'rlq' not in registers.keys(): registers['rlq'] = 0 
if 'rlq' not in registers.keys(): registers['rlq'] = 0 
inc('rlq', 744) if registers['rlq'] == -908 else do_nothing()
if registers['rlq'] > highest:
   highest = registers['rlq'] 
if 'qdq' not in registers.keys(): registers['qdq'] = 0 
if 'rlq' not in registers.keys(): registers['rlq'] = 0 
dec('qdq', -856) if registers['rlq'] >= -168 else do_nothing()
if registers['qdq'] > highest:
   highest = registers['qdq'] 
if 'wfk' not in registers.keys(): registers['wfk'] = 0 
if 'rlq' not in registers.keys(): registers['rlq'] = 0 
inc('wfk', -53) if registers['rlq'] <= -164 else do_nothing()
if registers['wfk'] > highest:
   highest = registers['wfk'] 
if 'bfx' not in registers.keys(): registers['bfx'] = 0 
if 'a' not in registers.keys(): registers['a'] = 0 
dec('bfx', 370) if registers['a'] == -378 else do_nothing()
if registers['bfx'] > highest:
   highest = registers['bfx'] 
if 'w' not in registers.keys(): registers['w'] = 0 
if 'lpi' not in registers.keys(): registers['lpi'] = 0 
dec('w', 388) if registers['lpi'] <= -812 else do_nothing()
if registers['w'] > highest:
   highest = registers['w'] 
if 'jh' not in registers.keys(): registers['jh'] = 0 
if 'a' not in registers.keys(): registers['a'] = 0 
inc('jh', -458) if registers['a'] <= -375 else do_nothing()
if registers['jh'] > highest:
   highest = registers['jh'] 
if 'ev' not in registers.keys(): registers['ev'] = 0 
if 'm' not in registers.keys(): registers['m'] = 0 
dec('ev', 169) if registers['m'] < -623 else do_nothing()
if registers['ev'] > highest:
   highest = registers['ev'] 
if 'afu' not in registers.keys(): registers['afu'] = 0 
if 'afu' not in registers.keys(): registers['afu'] = 0 
dec('afu', 673) if registers['afu'] <= 117 else do_nothing()
if registers['afu'] > highest:
   highest = registers['afu'] 
if 'jq' not in registers.keys(): registers['jq'] = 0 
if 'vh' not in registers.keys(): registers['vh'] = 0 
dec('jq', -294) if registers['vh'] >= -362 else do_nothing()
if registers['jq'] > highest:
   highest = registers['jq'] 
if 'ghj' not in registers.keys(): registers['ghj'] = 0 
if 'qn' not in registers.keys(): registers['qn'] = 0 
inc('ghj', -595) if registers['qn'] >= -711 else do_nothing()
if registers['ghj'] > highest:
   highest = registers['ghj'] 
if 'm' not in registers.keys(): registers['m'] = 0 
if 'lpi' not in registers.keys(): registers['lpi'] = 0 
inc('m', -292) if registers['lpi'] <= -823 else do_nothing()
if registers['m'] > highest:
   highest = registers['m'] 
if 'wfk' not in registers.keys(): registers['wfk'] = 0 
if 'pr' not in registers.keys(): registers['pr'] = 0 
inc('wfk', -401) if registers['pr'] >= -536 else do_nothing()
if registers['wfk'] > highest:
   highest = registers['wfk'] 
if 'w' not in registers.keys(): registers['w'] = 0 
if 'fkp' not in registers.keys(): registers['fkp'] = 0 
inc('w', -846) if registers['fkp'] <= 818 else do_nothing()
if registers['w'] > highest:
   highest = registers['w'] 
if 'afu' not in registers.keys(): registers['afu'] = 0 
if 'fkp' not in registers.keys(): registers['fkp'] = 0 
inc('afu', 224) if registers['fkp'] <= 825 else do_nothing()
if registers['afu'] > highest:
   highest = registers['afu'] 
if 'qdq' not in registers.keys(): registers['qdq'] = 0 
if 'fkp' not in registers.keys(): registers['fkp'] = 0 
dec('qdq', -22) if registers['fkp'] != 816 else do_nothing()
if registers['qdq'] > highest:
   highest = registers['qdq'] 
if 'bfx' not in registers.keys(): registers['bfx'] = 0 
if 'qn' not in registers.keys(): registers['qn'] = 0 
inc('bfx', 148) if registers['qn'] == -713 else do_nothing()
if registers['bfx'] > highest:
   highest = registers['bfx'] 
if 'qrc' not in registers.keys(): registers['qrc'] = 0 
if 'lpi' not in registers.keys(): registers['lpi'] = 0 
inc('qrc', -253) if registers['lpi'] >= -815 else do_nothing()
if registers['qrc'] > highest:
   highest = registers['qrc'] 
if 'w' not in registers.keys(): registers['w'] = 0 
if 'fkp' not in registers.keys(): registers['fkp'] = 0 
inc('w', -824) if registers['fkp'] != 816 else do_nothing()
if registers['w'] > highest:
   highest = registers['w'] 
if 'jq' not in registers.keys(): registers['jq'] = 0 
if 'wfk' not in registers.keys(): registers['wfk'] = 0 
inc('jq', 409) if registers['wfk'] <= 821 else do_nothing()
if registers['jq'] > highest:
   highest = registers['jq'] 
if 'a' not in registers.keys(): registers['a'] = 0 
if 'ev' not in registers.keys(): registers['ev'] = 0 
inc('a', -243) if registers['ev'] < -1044 else do_nothing()
if registers['a'] > highest:
   highest = registers['a'] 
if 'ev' not in registers.keys(): registers['ev'] = 0 
if 'afu' not in registers.keys(): registers['afu'] = 0 
inc('ev', 784) if registers['afu'] <= -329 else do_nothing()
if registers['ev'] > highest:
   highest = registers['ev'] 
if 'a' not in registers.keys(): registers['a'] = 0 
if 'a' not in registers.keys(): registers['a'] = 0 
inc('a', 492) if registers['a'] > -625 else do_nothing()
if registers['a'] > highest:
   highest = registers['a'] 
if 'qrc' not in registers.keys(): registers['qrc'] = 0 
if 'afu' not in registers.keys(): registers['afu'] = 0 
dec('qrc', 675) if registers['afu'] != -327 else do_nothing()
if registers['qrc'] > highest:
   highest = registers['qrc'] 
if 'yo' not in registers.keys(): registers['yo'] = 0 
if 'g' not in registers.keys(): registers['g'] = 0 
inc('yo', -902) if registers['g'] > -623 else do_nothing()
if registers['yo'] > highest:
   highest = registers['yo'] 
if 'jh' not in registers.keys(): registers['jh'] = 0 
if 'm' not in registers.keys(): registers['m'] = 0 
inc('jh', -341) if registers['m'] <= -632 else do_nothing()
if registers['jh'] > highest:
   highest = registers['jh'] 
if 'rlq' not in registers.keys(): registers['rlq'] = 0 
if 'g' not in registers.keys(): registers['g'] = 0 
inc('rlq', 139) if registers['g'] > -622 else do_nothing()
if registers['rlq'] > highest:
   highest = registers['rlq'] 
if 'qdq' not in registers.keys(): registers['qdq'] = 0 
if 'vh' not in registers.keys(): registers['vh'] = 0 
inc('qdq', -156) if registers['vh'] <= -355 else do_nothing()
if registers['qdq'] > highest:
   highest = registers['qdq'] 
if 'ev' not in registers.keys(): registers['ev'] = 0 
if 'qdq' not in registers.keys(): registers['qdq'] = 0 
inc('ev', 105) if registers['qdq'] > 1646 else do_nothing()
if registers['ev'] > highest:
   highest = registers['ev'] 
if 'g' not in registers.keys(): registers['g'] = 0 
if 'u' not in registers.keys(): registers['u'] = 0 
dec('g', -334) if registers['u'] < -981 else do_nothing()
if registers['g'] > highest:
   highest = registers['g'] 
if 'qn' not in registers.keys(): registers['qn'] = 0 
if 'lpi' not in registers.keys(): registers['lpi'] = 0 
inc('qn', -117) if registers['lpi'] < -810 else do_nothing()
if registers['qn'] > highest:
   highest = registers['qn'] 
if 'fkp' not in registers.keys(): registers['fkp'] = 0 
if 'jq' not in registers.keys(): registers['jq'] = 0 
dec('fkp', -419) if registers['jq'] > 3687 else do_nothing()
if registers['fkp'] > highest:
   highest = registers['fkp'] 
if 'lpi' not in registers.keys(): registers['lpi'] = 0 
if 'wfk' not in registers.keys(): registers['wfk'] = 0 
inc('lpi', 950) if registers['wfk'] <= 830 else do_nothing()
if registers['lpi'] > highest:
   highest = registers['lpi'] 
if 'm' not in registers.keys(): registers['m'] = 0 
if 'k' not in registers.keys(): registers['k'] = 0 
inc('m', 305) if registers['k'] <= -224 else do_nothing()
if registers['m'] > highest:
   highest = registers['m'] 
if 'yo' not in registers.keys(): registers['yo'] = 0 
if 'vh' not in registers.keys(): registers['vh'] = 0 
inc('yo', -355) if registers['vh'] != -365 else do_nothing()
if registers['yo'] > highest:
   highest = registers['yo'] 
if 'jh' not in registers.keys(): registers['jh'] = 0 
if 't' not in registers.keys(): registers['t'] = 0 
dec('jh', 775) if registers['t'] < -1710 else do_nothing()
if registers['jh'] > highest:
   highest = registers['jh'] 
if 'qrc' not in registers.keys(): registers['qrc'] = 0 
if 'nkr' not in registers.keys(): registers['nkr'] = 0 
dec('qrc', 125) if registers['nkr'] > -2054 else do_nothing()
if registers['qrc'] > highest:
   highest = registers['qrc'] 
if 'lpi' not in registers.keys(): registers['lpi'] = 0 
if 'nkr' not in registers.keys(): registers['nkr'] = 0 
inc('lpi', 572) if registers['nkr'] <= -2049 else do_nothing()
if registers['lpi'] > highest:
   highest = registers['lpi'] 
if 'rlq' not in registers.keys(): registers['rlq'] = 0 
if 'ghj' not in registers.keys(): registers['ghj'] = 0 
dec('rlq', 913) if registers['ghj'] <= 791 else do_nothing()
if registers['rlq'] > highest:
   highest = registers['rlq'] 
if 'g' not in registers.keys(): registers['g'] = 0 
if 'm' not in registers.keys(): registers['m'] = 0 
dec('g', -25) if registers['m'] >= -330 else do_nothing()
if registers['g'] > highest:
   highest = registers['g'] 
if 'bfx' not in registers.keys(): registers['bfx'] = 0 
if 'ev' not in registers.keys(): registers['ev'] = 0 
dec('bfx', -973) if registers['ev'] == -161 else do_nothing()
if registers['bfx'] > highest:
   highest = registers['bfx'] 
if 'sh' not in registers.keys(): registers['sh'] = 0 
if 't' not in registers.keys(): registers['t'] = 0 
inc('sh', -500) if registers['t'] >= -1718 else do_nothing()
if registers['sh'] > highest:
   highest = registers['sh'] 
if 'afu' not in registers.keys(): registers['afu'] = 0 
if 'qn' not in registers.keys(): registers['qn'] = 0 
inc('afu', 496) if registers['qn'] < -820 else do_nothing()
if registers['afu'] > highest:
   highest = registers['afu'] 
if 'afu' not in registers.keys(): registers['afu'] = 0 
if 'vh' not in registers.keys(): registers['vh'] = 0 
inc('afu', 242) if registers['vh'] >= -365 else do_nothing()
if registers['afu'] > highest:
   highest = registers['afu'] 
if 't' not in registers.keys(): registers['t'] = 0 
if 'm' not in registers.keys(): registers['m'] = 0 
dec('t', -474) if registers['m'] == -328 else do_nothing()
if registers['t'] > highest:
   highest = registers['t'] 
if 'w' not in registers.keys(): registers['w'] = 0 
if 'g' not in registers.keys(): registers['g'] = 0 
dec('w', -597) if registers['g'] <= -587 else do_nothing()
if registers['w'] > highest:
   highest = registers['w'] 
if 'qdq' not in registers.keys(): registers['qdq'] = 0 
if 'jq' not in registers.keys(): registers['jq'] = 0 
dec('qdq', 681) if registers['jq'] == 3690 else do_nothing()
if registers['qdq'] > highest:
   highest = registers['qdq'] 
if 'k' not in registers.keys(): registers['k'] = 0 
if 'bfx' not in registers.keys(): registers['bfx'] = 0 
dec('k', -349) if registers['bfx'] != 1530 else do_nothing()
if registers['k'] > highest:
   highest = registers['k'] 
if 'pr' not in registers.keys(): registers['pr'] = 0 
if 'yo' not in registers.keys(): registers['yo'] = 0 
inc('pr', -430) if registers['yo'] != -1595 else do_nothing()
if registers['pr'] > highest:
   highest = registers['pr'] 
if 'nkr' not in registers.keys(): registers['nkr'] = 0 
if 'afu' not in registers.keys(): registers['afu'] = 0 
inc('nkr', 105) if registers['afu'] != 410 else do_nothing()
if registers['nkr'] > highest:
   highest = registers['nkr'] 
if 'w' not in registers.keys(): registers['w'] = 0 
if 'jh' not in registers.keys(): registers['jh'] = 0 
dec('w', -788) if registers['jh'] < -1272 else do_nothing()
if registers['w'] > highest:
   highest = registers['w'] 
if 'lpi' not in registers.keys(): registers['lpi'] = 0 
if 'ghj' not in registers.keys(): registers['ghj'] = 0 
inc('lpi', 328) if registers['ghj'] >= 785 else do_nothing()
if registers['lpi'] > highest:
   highest = registers['lpi'] 
if 'rlq' not in registers.keys(): registers['rlq'] = 0 
if 'vh' not in registers.keys(): registers['vh'] = 0 
inc('rlq', 694) if registers['vh'] <= -368 else do_nothing()
if registers['rlq'] > highest:
   highest = registers['rlq'] 
if 'a' not in registers.keys(): registers['a'] = 0 
if 'ev' not in registers.keys(): registers['ev'] = 0 
inc('a', 965) if registers['ev'] != -168 else do_nothing()
if registers['a'] > highest:
   highest = registers['a'] 
if 'g' not in registers.keys(): registers['g'] = 0 
if 'jq' not in registers.keys(): registers['jq'] = 0 
inc('g', -962) if registers['jq'] < 3690 else do_nothing()
if registers['g'] > highest:
   highest = registers['g'] 
if 'pr' not in registers.keys(): registers['pr'] = 0 
if 'lpi' not in registers.keys(): registers['lpi'] = 0 
inc('pr', -181) if registers['lpi'] == 1035 else do_nothing()
if registers['pr'] > highest:
   highest = registers['pr'] 
if 'rlq' not in registers.keys(): registers['rlq'] = 0 
if 'rlq' not in registers.keys(): registers['rlq'] = 0 
dec('rlq', 509) if registers['rlq'] >= -947 else do_nothing()
if registers['rlq'] > highest:
   highest = registers['rlq'] 
if 'k' not in registers.keys(): registers['k'] = 0 
if 'w' not in registers.keys(): registers['w'] = 0 
dec('k', -991) if registers['w'] >= -1573 else do_nothing()
if registers['k'] > highest:
   highest = registers['k'] 
if 'bfx' not in registers.keys(): registers['bfx'] = 0 
if 'qrc' not in registers.keys(): registers['qrc'] = 0 
dec('bfx', -516) if registers['qrc'] < -816 else do_nothing()
if registers['bfx'] > highest:
   highest = registers['bfx'] 
if 'a' not in registers.keys(): registers['a'] = 0 
if 'qdq' not in registers.keys(): registers['qdq'] = 0 
dec('a', 679) if registers['qdq'] == 961 else do_nothing()
if registers['a'] > highest:
   highest = registers['a'] 
if 'lpi' not in registers.keys(): registers['lpi'] = 0 
if 'jh' not in registers.keys(): registers['jh'] = 0 
inc('lpi', -640) if registers['jh'] <= -1273 else do_nothing()
if registers['lpi'] > highest:
   highest = registers['lpi'] 
if 'w' not in registers.keys(): registers['w'] = 0 
if 'rlq' not in registers.keys(): registers['rlq'] = 0 
dec('w', -13) if registers['rlq'] >= -1440 else do_nothing()
if registers['w'] > highest:
   highest = registers['w'] 
if 'm' not in registers.keys(): registers['m'] = 0 
if 'lpi' not in registers.keys(): registers['lpi'] = 0 
dec('m', 535) if registers['lpi'] > 402 else do_nothing()
if registers['m'] > highest:
   highest = registers['m'] 
if 'sh' not in registers.keys(): registers['sh'] = 0 
if 't' not in registers.keys(): registers['t'] = 0 
dec('sh', -358) if registers['t'] > -1241 else do_nothing()
if registers['sh'] > highest:
   highest = registers['sh'] 
if 'qdq' not in registers.keys(): registers['qdq'] = 0 
if 'wfk' not in registers.keys(): registers['wfk'] = 0 
inc('qdq', -647) if registers['wfk'] > 821 else do_nothing()
if registers['qdq'] > highest:
   highest = registers['qdq'] 
if 'u' not in registers.keys(): registers['u'] = 0 
if 'a' not in registers.keys(): registers['a'] = 0 
dec('u', 409) if registers['a'] < 838 else do_nothing()
if registers['u'] > highest:
   highest = registers['u'] 
if 'lpi' not in registers.keys(): registers['lpi'] = 0 
if 'wfk' not in registers.keys(): registers['wfk'] = 0 
dec('lpi', 745) if registers['wfk'] < 832 else do_nothing()
if registers['lpi'] > highest:
   highest = registers['lpi'] 
if 'yo' not in registers.keys(): registers['yo'] = 0 
if 'w' not in registers.keys(): registers['w'] = 0 
dec('yo', 422) if registers['w'] < -1564 else do_nothing()
if registers['yo'] > highest:
   highest = registers['yo'] 
if 'jq' not in registers.keys(): registers['jq'] = 0 
if 'm' not in registers.keys(): registers['m'] = 0 
dec('jq', 555) if registers['m'] > -319 else do_nothing()
if registers['jq'] > highest:
   highest = registers['jq'] 
if 'fkp' not in registers.keys(): registers['fkp'] = 0 
if 'qrc' not in registers.keys(): registers['qrc'] = 0 
inc('fkp', 202) if registers['qrc'] < -805 else do_nothing()
if registers['fkp'] > highest:
   highest = registers['fkp'] 
if 'wfk' not in registers.keys(): registers['wfk'] = 0 
if 'vh' not in registers.keys(): registers['vh'] = 0 
dec('wfk', -52) if registers['vh'] == -355 else do_nothing()
if registers['wfk'] > highest:
   highest = registers['wfk'] 
if 'pr' not in registers.keys(): registers['pr'] = 0 
if 'jq' not in registers.keys(): registers['jq'] = 0 
inc('pr', 473) if registers['jq'] < 3699 else do_nothing()
if registers['pr'] > highest:
   highest = registers['pr'] 
if 'bfx' not in registers.keys(): registers['bfx'] = 0 
if 'pr' not in registers.keys(): registers['pr'] = 0 
dec('bfx', -202) if registers['pr'] > -674 else do_nothing()
if registers['bfx'] > highest:
   highest = registers['bfx'] 
if 'fkp' not in registers.keys(): registers['fkp'] = 0 
if 'ghj' not in registers.keys(): registers['ghj'] = 0 
inc('fkp', 907) if registers['ghj'] <= 787 else do_nothing()
if registers['fkp'] > highest:
   highest = registers['fkp'] 
if 'yo' not in registers.keys(): registers['yo'] = 0 
if 'rlq' not in registers.keys(): registers['rlq'] = 0 
inc('yo', -617) if registers['rlq'] > -1455 else do_nothing()
if registers['yo'] > highest:
   highest = registers['yo'] 
if 'jq' not in registers.keys(): registers['jq'] = 0 
if 'jq' not in registers.keys(): registers['jq'] = 0 
inc('jq', -300) if registers['jq'] != 3699 else do_nothing()
if registers['jq'] > highest:
   highest = registers['jq'] 
if 'u' not in registers.keys(): registers['u'] = 0 
if 'nkr' not in registers.keys(): registers['nkr'] = 0 
dec('u', 910) if registers['nkr'] < -1945 else do_nothing()
if registers['u'] > highest:
   highest = registers['u'] 
if 'g' not in registers.keys(): registers['g'] = 0 
if 'bfx' not in registers.keys(): registers['bfx'] = 0 
dec('g', -880) if registers['bfx'] < 1722 else do_nothing()
if registers['g'] > highest:
   highest = registers['g'] 
if 'ev' not in registers.keys(): registers['ev'] = 0 
if 'ev' not in registers.keys(): registers['ev'] = 0 
inc('ev', 47) if registers['ev'] > -166 else do_nothing()
if registers['ev'] > highest:
   highest = registers['ev'] 
if 'a' not in registers.keys(): registers['a'] = 0 
if 'afu' not in registers.keys(): registers['afu'] = 0 
inc('a', 372) if registers['afu'] == 404 else do_nothing()
if registers['a'] > highest:
   highest = registers['a'] 
if 'u' not in registers.keys(): registers['u'] = 0 
if 'qdq' not in registers.keys(): registers['qdq'] = 0 
inc('u', 318) if registers['qdq'] != 319 else do_nothing()
if registers['u'] > highest:
   highest = registers['u'] 
if 'afu' not in registers.keys(): registers['afu'] = 0 
if 'qdq' not in registers.keys(): registers['qdq'] = 0 
inc('afu', 942) if registers['qdq'] == 319 else do_nothing()
if registers['afu'] > highest:
   highest = registers['afu'] 
if 'sh' not in registers.keys(): registers['sh'] = 0 
if 'ghj' not in registers.keys(): registers['ghj'] = 0 
dec('sh', 522) if registers['ghj'] <= 793 else do_nothing()
if registers['sh'] > highest:
   highest = registers['sh'] 
if 'm' not in registers.keys(): registers['m'] = 0 
if 'g' not in registers.keys(): registers['g'] = 0 
dec('m', -785) if registers['g'] <= -588 else do_nothing()
if registers['m'] > highest:
   highest = registers['m'] 
if 'pr' not in registers.keys(): registers['pr'] = 0 
if 'qrc' not in registers.keys(): registers['qrc'] = 0 
dec('pr', 878) if registers['qrc'] <= -805 else do_nothing()
if registers['pr'] > highest:
   highest = registers['pr'] 
if 'a' not in registers.keys(): registers['a'] = 0 
if 'm' not in registers.keys(): registers['m'] = 0 
inc('a', -812) if registers['m'] != 452 else do_nothing()
if registers['a'] > highest:
   highest = registers['a'] 
if 'wfk' not in registers.keys(): registers['wfk'] = 0 
if 'lpi' not in registers.keys(): registers['lpi'] = 0 
dec('wfk', -695) if registers['lpi'] >= -355 else do_nothing()
if registers['wfk'] > highest:
   highest = registers['wfk'] 
if 'qdq' not in registers.keys(): registers['qdq'] = 0 
if 'jh' not in registers.keys(): registers['jh'] = 0 
dec('qdq', -493) if registers['jh'] >= -1279 else do_nothing()
if registers['qdq'] > highest:
   highest = registers['qdq'] 
if 'pr' not in registers.keys(): registers['pr'] = 0 
if 'k' not in registers.keys(): registers['k'] = 0 
dec('pr', 325) if registers['k'] < 1115 else do_nothing()
if registers['pr'] > highest:
   highest = registers['pr'] 
if 'nkr' not in registers.keys(): registers['nkr'] = 0 
if 'sh' not in registers.keys(): registers['sh'] = 0 
inc('nkr', 581) if registers['sh'] >= -333 else do_nothing()
if registers['nkr'] > highest:
   highest = registers['nkr'] 
if 'a' not in registers.keys(): registers['a'] = 0 
if 'pr' not in registers.keys(): registers['pr'] = 0 
dec('a', -368) if registers['pr'] == -1861 else do_nothing()
if registers['a'] > highest:
   highest = registers['a'] 
if 'ghj' not in registers.keys(): registers['ghj'] = 0 
if 'qn' not in registers.keys(): registers['qn'] = 0 
dec('ghj', 135) if registers['qn'] >= -835 else do_nothing()
if registers['ghj'] > highest:
   highest = registers['ghj'] 
if 'jh' not in registers.keys(): registers['jh'] = 0 
if 'a' not in registers.keys(): registers['a'] = 0 
dec('jh', -209) if registers['a'] < 406 else do_nothing()
if registers['jh'] > highest:
   highest = registers['jh'] 
if 'u' not in registers.keys(): registers['u'] = 0 
if 'lpi' not in registers.keys(): registers['lpi'] = 0 
dec('u', -518) if registers['lpi'] > -352 else do_nothing()
if registers['u'] > highest:
   highest = registers['u'] 
if 'qdq' not in registers.keys(): registers['qdq'] = 0 
if 't' not in registers.keys(): registers['t'] = 0 
inc('qdq', 598) if registers['t'] > -1239 else do_nothing()
if registers['qdq'] > highest:
   highest = registers['qdq'] 
if 'k' not in registers.keys(): registers['k'] = 0 
if 'm' not in registers.keys(): registers['m'] = 0 
dec('k', -879) if registers['m'] != 459 else do_nothing()
if registers['k'] > highest:
   highest = registers['k'] 
if 'fkp' not in registers.keys(): registers['fkp'] = 0 
if 'nkr' not in registers.keys(): registers['nkr'] = 0 
dec('fkp', -587) if registers['nkr'] == -1366 else do_nothing()
if registers['fkp'] > highest:
   highest = registers['fkp'] 
if 'yo' not in registers.keys(): registers['yo'] = 0 
if 'qrc' not in registers.keys(): registers['qrc'] = 0 
dec('yo', -902) if registers['qrc'] <= -806 else do_nothing()
if registers['yo'] > highest:
   highest = registers['yo'] 
if 'nkr' not in registers.keys(): registers['nkr'] = 0 
if 'yo' not in registers.keys(): registers['yo'] = 0 
dec('nkr', -948) if registers['yo'] == -1739 else do_nothing()
if registers['nkr'] > highest:
   highest = registers['nkr'] 
if 'pr' not in registers.keys(): registers['pr'] = 0 
if 'k' not in registers.keys(): registers['k'] = 0 
inc('pr', -317) if registers['k'] != 1998 else do_nothing()
if registers['pr'] > highest:
   highest = registers['pr'] 
if 'ghj' not in registers.keys(): registers['ghj'] = 0 
if 'bfx' not in registers.keys(): registers['bfx'] = 0 
inc('ghj', 535) if registers['bfx'] == 1722 else do_nothing()
if registers['ghj'] > highest:
   highest = registers['ghj'] 
if 'nkr' not in registers.keys(): registers['nkr'] = 0 
if 'vh' not in registers.keys(): registers['vh'] = 0 
inc('nkr', -72) if registers['vh'] == -360 else do_nothing()
if registers['nkr'] > highest:
   highest = registers['nkr'] 
if 'ev' not in registers.keys(): registers['ev'] = 0 
if 'rlq' not in registers.keys(): registers['rlq'] = 0 
dec('ev', -234) if registers['rlq'] != -1455 else do_nothing()
if registers['ev'] > highest:
   highest = registers['ev'] 
if 'a' not in registers.keys(): registers['a'] = 0 
if 'k' not in registers.keys(): registers['k'] = 0 
dec('a', 869) if registers['k'] == 1992 else do_nothing()
if registers['a'] > highest:
   highest = registers['a'] 
if 'ev' not in registers.keys(): registers['ev'] = 0 
if 'yo' not in registers.keys(): registers['yo'] = 0 
inc('ev', -397) if registers['yo'] >= -1746 else do_nothing()
if registers['ev'] > highest:
   highest = registers['ev'] 
if 'bfx' not in registers.keys(): registers['bfx'] = 0 
if 'bfx' not in registers.keys(): registers['bfx'] = 0 
dec('bfx', 642) if registers['bfx'] <= 1734 else do_nothing()
if registers['bfx'] > highest:
   highest = registers['bfx'] 
if 'jq' not in registers.keys(): registers['jq'] = 0 
if 'jh' not in registers.keys(): registers['jh'] = 0 
dec('jq', 501) if registers['jh'] <= -1057 else do_nothing()
if registers['jq'] > highest:
   highest = registers['jq'] 
if 'w' not in registers.keys(): registers['w'] = 0 
if 'qdq' not in registers.keys(): registers['qdq'] = 0 
inc('w', 900) if registers['qdq'] == 1410 else do_nothing()
if registers['w'] > highest:
   highest = registers['w'] 
if 'lpi' not in registers.keys(): registers['lpi'] = 0 
if 'ev' not in registers.keys(): registers['ev'] = 0 
dec('lpi', 742) if registers['ev'] >= -277 else do_nothing()
if registers['lpi'] > highest:
   highest = registers['lpi'] 
if 'pr' not in registers.keys(): registers['pr'] = 0 
if 'rlq' not in registers.keys(): registers['rlq'] = 0 
dec('pr', 842) if registers['rlq'] != -1441 else do_nothing()
if registers['pr'] > highest:
   highest = registers['pr'] 
if 'qdq' not in registers.keys(): registers['qdq'] = 0 
if 'a' not in registers.keys(): registers['a'] = 0 
inc('qdq', -56) if registers['a'] == -473 else do_nothing()
if registers['qdq'] > highest:
   highest = registers['qdq'] 
if 'jh' not in registers.keys(): registers['jh'] = 0 
if 'a' not in registers.keys(): registers['a'] = 0 
dec('jh', -421) if registers['a'] != -470 else do_nothing()
if registers['jh'] > highest:
   highest = registers['jh'] 
if 'jq' not in registers.keys(): registers['jq'] = 0 
if 'k' not in registers.keys(): registers['k'] = 0 
inc('jq', 60) if registers['k'] >= 1997 else do_nothing()
if registers['jq'] > highest:
   highest = registers['jq'] 
if 'lpi' not in registers.keys(): registers['lpi'] = 0 
if 'g' not in registers.keys(): registers['g'] = 0 
inc('lpi', 181) if registers['g'] <= -592 else do_nothing()
if registers['lpi'] > highest:
   highest = registers['lpi'] 
if 'jh' not in registers.keys(): registers['jh'] = 0 
if 'afu' not in registers.keys(): registers['afu'] = 0 
inc('jh', -888) if registers['afu'] < 1349 else do_nothing()
if registers['jh'] > highest:
   highest = registers['jh'] 
if 'w' not in registers.keys(): registers['w'] = 0 
if 'lpi' not in registers.keys(): registers['lpi'] = 0 
inc('w', 271) if registers['lpi'] >= -912 else do_nothing()
if registers['w'] > highest:
   highest = registers['w'] 
if 'wfk' not in registers.keys(): registers['wfk'] = 0 
if 'jq' not in registers.keys(): registers['jq'] = 0 
dec('wfk', 319) if registers['jq'] <= 2890 else do_nothing()
if registers['wfk'] > highest:
   highest = registers['wfk'] 
if 'qrc' not in registers.keys(): registers['qrc'] = 0 
if 'vh' not in registers.keys(): registers['vh'] = 0 
inc('qrc', 144) if registers['vh'] >= -368 else do_nothing()
if registers['qrc'] > highest:
   highest = registers['qrc'] 
if 'rlq' not in registers.keys(): registers['rlq'] = 0 
if 'nkr' not in registers.keys(): registers['nkr'] = 0 
dec('rlq', 263) if registers['nkr'] <= -492 else do_nothing()
if registers['rlq'] > highest:
   highest = registers['rlq'] 
if 'sh' not in registers.keys(): registers['sh'] = 0 
if 'wfk' not in registers.keys(): registers['wfk'] = 0 
inc('sh', 214) if registers['wfk'] <= 1208 else do_nothing()
if registers['sh'] > highest:
   highest = registers['sh'] 
if 'k' not in registers.keys(): registers['k'] = 0 
if 'qrc' not in registers.keys(): registers['qrc'] = 0 
inc('k', -39) if registers['qrc'] < -673 else do_nothing()
if registers['k'] > highest:
   highest = registers['k'] 
if 'rlq' not in registers.keys(): registers['rlq'] = 0 
if 'qn' not in registers.keys(): registers['qn'] = 0 
dec('rlq', -388) if registers['qn'] == -830 else do_nothing()
if registers['rlq'] > highest:
   highest = registers['rlq'] 
if 'fkp' not in registers.keys(): registers['fkp'] = 0 
if 'vh' not in registers.keys(): registers['vh'] = 0 
inc('fkp', 917) if registers['vh'] > -366 else do_nothing()
if registers['fkp'] > highest:
   highest = registers['fkp'] 
if 'u' not in registers.keys(): registers['u'] = 0 
if 'qrc' not in registers.keys(): registers['qrc'] = 0 
dec('u', -225) if registers['qrc'] < -663 else do_nothing()
if registers['u'] > highest:
   highest = registers['u'] 
if 'lpi' not in registers.keys(): registers['lpi'] = 0 
if 'u' not in registers.keys(): registers['u'] = 0 
dec('lpi', -741) if registers['u'] > -1550 else do_nothing()
if registers['lpi'] > highest:
   highest = registers['lpi'] 
if 'lpi' not in registers.keys(): registers['lpi'] = 0 
if 'afu' not in registers.keys(): registers['afu'] = 0 
inc('lpi', -176) if registers['afu'] <= 1354 else do_nothing()
if registers['lpi'] > highest:
   highest = registers['lpi'] 
if 'u' not in registers.keys(): registers['u'] = 0 
if 'k' not in registers.keys(): registers['k'] = 0 
inc('u', 454) if registers['k'] <= 1995 else do_nothing()
if registers['u'] > highest:
   highest = registers['u'] 
if 'qn' not in registers.keys(): registers['qn'] = 0 
if 'rlq' not in registers.keys(): registers['rlq'] = 0 
inc('qn', 623) if registers['rlq'] >= -1059 else do_nothing()
if registers['qn'] > highest:
   highest = registers['qn'] 
if 'fkp' not in registers.keys(): registers['fkp'] = 0 
if 'nkr' not in registers.keys(): registers['nkr'] = 0 
inc('fkp', 642) if registers['nkr'] < -485 else do_nothing()
if registers['fkp'] > highest:
   highest = registers['fkp'] 
if 'jh' not in registers.keys(): registers['jh'] = 0 
if 'pr' not in registers.keys(): registers['pr'] = 0 
dec('jh', 895) if registers['pr'] < -3027 else do_nothing()
if registers['jh'] > highest:
   highest = registers['jh'] 
if 'k' not in registers.keys(): registers['k'] = 0 
if 'fkp' not in registers.keys(): registers['fkp'] = 0 
dec('k', 240) if registers['fkp'] < 3592 else do_nothing()
if registers['k'] > highest:
   highest = registers['k'] 
if 'afu' not in registers.keys(): registers['afu'] = 0 
if 'vh' not in registers.keys(): registers['vh'] = 0 
dec('afu', 772) if registers['vh'] < -367 else do_nothing()
if registers['afu'] > highest:
   highest = registers['afu'] 
if 'nkr' not in registers.keys(): registers['nkr'] = 0 
if 'a' not in registers.keys(): registers['a'] = 0 
dec('nkr', 913) if registers['a'] < -467 else do_nothing()
if registers['nkr'] > highest:
   highest = registers['nkr'] 
if 'vh' not in registers.keys(): registers['vh'] = 0 
if 'lpi' not in registers.keys(): registers['lpi'] = 0 
inc('vh', -941) if registers['lpi'] != -336 else do_nothing()
if registers['vh'] > highest:
   highest = registers['vh'] 
if 'pr' not in registers.keys(): registers['pr'] = 0 
if 'nkr' not in registers.keys(): registers['nkr'] = 0 
inc('pr', -623) if registers['nkr'] != -1409 else do_nothing()
if registers['pr'] > highest:
   highest = registers['pr'] 
if 'g' not in registers.keys(): registers['g'] = 0 
if 'qdq' not in registers.keys(): registers['qdq'] = 0 
dec('g', 849) if registers['qdq'] != 1356 else do_nothing()
if registers['g'] > highest:
   highest = registers['g'] 
if 'bfx' not in registers.keys(): registers['bfx'] = 0 
if 't' not in registers.keys(): registers['t'] = 0 
dec('bfx', -647) if registers['t'] >= -1240 else do_nothing()
if registers['bfx'] > highest:
   highest = registers['bfx'] 
if 'jh' not in registers.keys(): registers['jh'] = 0 
if 'w' not in registers.keys(): registers['w'] = 0 
dec('jh', 654) if registers['w'] != -398 else do_nothing()
if registers['jh'] > highest:
   highest = registers['jh'] 
if 'a' not in registers.keys(): registers['a'] = 0 
if 'g' not in registers.keys(): registers['g'] = 0 
inc('a', -938) if registers['g'] != -1442 else do_nothing()
if registers['a'] > highest:
   highest = registers['a'] 
if 'jq' not in registers.keys(): registers['jq'] = 0 
if 'yo' not in registers.keys(): registers['yo'] = 0 
dec('jq', 545) if registers['yo'] > -1747 else do_nothing()
if registers['jq'] > highest:
   highest = registers['jq'] 
if 'qdq' not in registers.keys(): registers['qdq'] = 0 
if 'vh' not in registers.keys(): registers['vh'] = 0 
dec('qdq', 183) if registers['vh'] >= -1301 else do_nothing()
if registers['qdq'] > highest:
   highest = registers['qdq'] 
if 'fkp' not in registers.keys(): registers['fkp'] = 0 
if 'qn' not in registers.keys(): registers['qn'] = 0 
inc('fkp', -628) if registers['qn'] != -212 else do_nothing()
if registers['fkp'] > highest:
   highest = registers['fkp'] 
if 'u' not in registers.keys(): registers['u'] = 0 
if 'qdq' not in registers.keys(): registers['qdq'] = 0 
dec('u', -89) if registers['qdq'] == 1171 else do_nothing()
if registers['u'] > highest:
   highest = registers['u'] 
if 'qrc' not in registers.keys(): registers['qrc'] = 0 
if 'm' not in registers.keys(): registers['m'] = 0 
inc('qrc', -623) if registers['m'] > 448 else do_nothing()
if registers['qrc'] > highest:
   highest = registers['qrc'] 
if 'pr' not in registers.keys(): registers['pr'] = 0 
if 't' not in registers.keys(): registers['t'] = 0 
inc('pr', 61) if registers['t'] < -1237 else do_nothing()
if registers['pr'] > highest:
   highest = registers['pr'] 
if 'u' not in registers.keys(): registers['u'] = 0 
if 'qn' not in registers.keys(): registers['qn'] = 0 
dec('u', 83) if registers['qn'] < -204 else do_nothing()
if registers['u'] > highest:
   highest = registers['u'] 
if 'qrc' not in registers.keys(): registers['qrc'] = 0 
if 'm' not in registers.keys(): registers['m'] = 0 
inc('qrc', 179) if registers['m'] <= 466 else do_nothing()
if registers['qrc'] > highest:
   highest = registers['qrc'] 
if 'nkr' not in registers.keys(): registers['nkr'] = 0 
if 'nkr' not in registers.keys(): registers['nkr'] = 0 
dec('nkr', 2) if registers['nkr'] != -1408 else do_nothing()
if registers['nkr'] > highest:
   highest = registers['nkr'] 
if 'fkp' not in registers.keys(): registers['fkp'] = 0 
if 'u' not in registers.keys(): registers['u'] = 0 
dec('fkp', 813) if registers['u'] >= -1094 else do_nothing()
if registers['fkp'] > highest:
   highest = registers['fkp'] 
if 'sh' not in registers.keys(): registers['sh'] = 0 
if 'sh' not in registers.keys(): registers['sh'] = 0 
dec('sh', -127) if registers['sh'] < -111 else do_nothing()
if registers['sh'] > highest:
   highest = registers['sh'] 
if 'qdq' not in registers.keys(): registers['qdq'] = 0 
if 'rlq' not in registers.keys(): registers['rlq'] = 0 
dec('qdq', 697) if registers['rlq'] <= -1069 else do_nothing()
if registers['qdq'] > highest:
   highest = registers['qdq'] 
if 't' not in registers.keys(): registers['t'] = 0 
if 'k' not in registers.keys(): registers['k'] = 0 
dec('t', 191) if registers['k'] == 1752 else do_nothing()
if registers['t'] > highest:
   highest = registers['t'] 
if 'u' not in registers.keys(): registers['u'] = 0 
if 'bfx' not in registers.keys(): registers['bfx'] = 0 
dec('u', 352) if registers['bfx'] != 1725 else do_nothing()
if registers['u'] > highest:
   highest = registers['u'] 
if 'nkr' not in registers.keys(): registers['nkr'] = 0 
if 'fkp' not in registers.keys(): registers['fkp'] = 0 
inc('nkr', 188) if registers['fkp'] == 2145 else do_nothing()
if registers['nkr'] > highest:
   highest = registers['nkr'] 
if 'qn' not in registers.keys(): registers['qn'] = 0 
if 'wfk' not in registers.keys(): registers['wfk'] = 0 
inc('qn', -300) if registers['wfk'] >= 1192 else do_nothing()
if registers['qn'] > highest:
   highest = registers['qn'] 
if 'nkr' not in registers.keys(): registers['nkr'] = 0 
if 'jq' not in registers.keys(): registers['jq'] = 0 
dec('nkr', -520) if registers['jq'] >= 2345 else do_nothing()
if registers['nkr'] > highest:
   highest = registers['nkr'] 
if 'pr' not in registers.keys(): registers['pr'] = 0 
if 'g' not in registers.keys(): registers['g'] = 0 
dec('pr', 957) if registers['g'] < -1446 else do_nothing()
if registers['pr'] > highest:
   highest = registers['pr'] 
if 'g' not in registers.keys(): registers['g'] = 0 
if 'g' not in registers.keys(): registers['g'] = 0 
inc('g', -2) if registers['g'] <= -1436 else do_nothing()
if registers['g'] > highest:
   highest = registers['g'] 
if 'w' not in registers.keys(): registers['w'] = 0 
if 'vh' not in registers.keys(): registers['vh'] = 0 
dec('w', -64) if registers['vh'] <= -1307 else do_nothing()
if registers['w'] > highest:
   highest = registers['w'] 
if 'qn' not in registers.keys(): registers['qn'] = 0 
if 'w' not in registers.keys(): registers['w'] = 0 
inc('qn', 290) if registers['w'] < -387 else do_nothing()
if registers['qn'] > highest:
   highest = registers['qn'] 
if 'yo' not in registers.keys(): registers['yo'] = 0 
if 'bfx' not in registers.keys(): registers['bfx'] = 0 
dec('yo', -511) if registers['bfx'] > 1726 else do_nothing()
if registers['yo'] > highest:
   highest = registers['yo'] 
if 'qrc' not in registers.keys(): registers['qrc'] = 0 
if 'bfx' not in registers.keys(): registers['bfx'] = 0 
inc('qrc', -534) if registers['bfx'] < 1742 else do_nothing()
if registers['qrc'] > highest:
   highest = registers['qrc'] 
if 'fkp' not in registers.keys(): registers['fkp'] = 0 
if 'qn' not in registers.keys(): registers['qn'] = 0 
dec('fkp', 456) if registers['qn'] == -226 else do_nothing()
if registers['fkp'] > highest:
   highest = registers['fkp'] 
if 'ev' not in registers.keys(): registers['ev'] = 0 
if 'pr' not in registers.keys(): registers['pr'] = 0 
dec('ev', 409) if registers['pr'] > -3597 else do_nothing()
if registers['ev'] > highest:
   highest = registers['ev'] 
if 'k' not in registers.keys(): registers['k'] = 0 
if 'lpi' not in registers.keys(): registers['lpi'] = 0 
dec('k', 457) if registers['lpi'] > -348 else do_nothing()
if registers['k'] > highest:
   highest = registers['k'] 
if 't' not in registers.keys(): registers['t'] = 0 
if 'bfx' not in registers.keys(): registers['bfx'] = 0 
inc('t', -705) if registers['bfx'] > 1728 else do_nothing()
if registers['t'] > highest:
   highest = registers['t'] 
if 'a' not in registers.keys(): registers['a'] = 0 
if 'u' not in registers.keys(): registers['u'] = 0 
dec('a', 935) if registers['u'] >= -1450 else do_nothing()
if registers['a'] > highest:
   highest = registers['a'] 
if 'a' not in registers.keys(): registers['a'] = 0 
if 'vh' not in registers.keys(): registers['vh'] = 0 
inc('a', -904) if registers['vh'] > -1309 else do_nothing()
if registers['a'] > highest:
   highest = registers['a'] 
if 'ev' not in registers.keys(): registers['ev'] = 0 
if 'u' not in registers.keys(): registers['u'] = 0 
inc('ev', 873) if registers['u'] < -1434 else do_nothing()
if registers['ev'] > highest:
   highest = registers['ev'] 
if 'm' not in registers.keys(): registers['m'] = 0 
if 'k' not in registers.keys(): registers['k'] = 0 
inc('m', 704) if registers['k'] != 1286 else do_nothing()
if registers['m'] > highest:
   highest = registers['m'] 
if 'm' not in registers.keys(): registers['m'] = 0 
if 'qn' not in registers.keys(): registers['qn'] = 0 
inc('m', -331) if registers['qn'] > -213 else do_nothing()
if registers['m'] > highest:
   highest = registers['m'] 
if 't' not in registers.keys(): registers['t'] = 0 
if 'm' not in registers.keys(): registers['m'] = 0 
inc('t', -5) if registers['m'] <= 1161 else do_nothing()
if registers['t'] > highest:
   highest = registers['t'] 
if 'yo' not in registers.keys(): registers['yo'] = 0 
if 'rlq' not in registers.keys(): registers['rlq'] = 0 
dec('yo', 153) if registers['rlq'] >= -1066 else do_nothing()
if registers['yo'] > highest:
   highest = registers['yo'] 
if 'qn' not in registers.keys(): registers['qn'] = 0 
if 'u' not in registers.keys(): registers['u'] = 0 
dec('qn', -693) if registers['u'] <= -1436 else do_nothing()
if registers['qn'] > highest:
   highest = registers['qn'] 
if 'w' not in registers.keys(): registers['w'] = 0 
if 'g' not in registers.keys(): registers['g'] = 0 
dec('w', -812) if registers['g'] > -1451 else do_nothing()
if registers['w'] > highest:
   highest = registers['w'] 
if 'ghj' not in registers.keys(): registers['ghj'] = 0 
if 'ev' not in registers.keys(): registers['ev'] = 0 
inc('ghj', -838) if registers['ev'] > 180 else do_nothing()
if registers['ghj'] > highest:
   highest = registers['ghj'] 
if 'vh' not in registers.keys(): registers['vh'] = 0 
if 'jh' not in registers.keys(): registers['jh'] = 0 
inc('vh', -462) if registers['jh'] <= -3077 else do_nothing()
if registers['vh'] > highest:
   highest = registers['vh'] 
if 'rlq' not in registers.keys(): registers['rlq'] = 0 
if 'bfx' not in registers.keys(): registers['bfx'] = 0 
inc('rlq', 806) if registers['bfx'] <= 1738 else do_nothing()
if registers['rlq'] > highest:
   highest = registers['rlq'] 
if 'nkr' not in registers.keys(): registers['nkr'] = 0 
if 'yo' not in registers.keys(): registers['yo'] = 0 
dec('nkr', 827) if registers['yo'] >= -1387 else do_nothing()
if registers['nkr'] > highest:
   highest = registers['nkr'] 
if 'sh' not in registers.keys(): registers['sh'] = 0 
if 'm' not in registers.keys(): registers['m'] = 0 
inc('sh', -200) if registers['m'] > 1154 else do_nothing()
if registers['sh'] > highest:
   highest = registers['sh'] 
if 'm' not in registers.keys(): registers['m'] = 0 
if 't' not in registers.keys(): registers['t'] = 0 
inc('m', 397) if registers['t'] == -2147 else do_nothing()
if registers['m'] > highest:
   highest = registers['m'] 
if 'qdq' not in registers.keys(): registers['qdq'] = 0 
if 'qrc' not in registers.keys(): registers['qrc'] = 0 
dec('qdq', -345) if registers['qrc'] == -1648 else do_nothing()
if registers['qdq'] > highest:
   highest = registers['qdq'] 
if 'ev' not in registers.keys(): registers['ev'] = 0 
if 'afu' not in registers.keys(): registers['afu'] = 0 
inc('ev', -238) if registers['afu'] > 1337 else do_nothing()
if registers['ev'] > highest:
   highest = registers['ev'] 
if 'ev' not in registers.keys(): registers['ev'] = 0 
if 'u' not in registers.keys(): registers['u'] = 0 
dec('ev', -284) if registers['u'] >= -1448 else do_nothing()
if registers['ev'] > highest:
   highest = registers['ev'] 
if 'g' not in registers.keys(): registers['g'] = 0 
if 'afu' not in registers.keys(): registers['afu'] = 0 
dec('g', 108) if registers['afu'] == 1346 else do_nothing()
if registers['g'] > highest:
   highest = registers['g'] 
if 'ghj' not in registers.keys(): registers['ghj'] = 0 
if 'ev' not in registers.keys(): registers['ev'] = 0 
inc('ghj', 291) if registers['ev'] != 230 else do_nothing()
if registers['ghj'] > highest:
   highest = registers['ghj'] 
if 'jh' not in registers.keys(): registers['jh'] = 0 
if 'rlq' not in registers.keys(): registers['rlq'] = 0 
inc('jh', -367) if registers['rlq'] == -253 else do_nothing()
if registers['jh'] > highest:
   highest = registers['jh'] 
if 'u' not in registers.keys(): registers['u'] = 0 
if 'm' not in registers.keys(): registers['m'] = 0 
inc('u', -88) if registers['m'] != 1164 else do_nothing()
if registers['u'] > highest:
   highest = registers['u'] 
if 'qrc' not in registers.keys(): registers['qrc'] = 0 
if 'm' not in registers.keys(): registers['m'] = 0 
inc('qrc', -513) if registers['m'] >= 1160 else do_nothing()
if registers['qrc'] > highest:
   highest = registers['qrc'] 
if 'm' not in registers.keys(): registers['m'] = 0 
if 'bfx' not in registers.keys(): registers['bfx'] = 0 
inc('m', 428) if registers['bfx'] == 1734 else do_nothing()
if registers['m'] > highest:
   highest = registers['m'] 
if 'wfk' not in registers.keys(): registers['wfk'] = 0 
if 'w' not in registers.keys(): registers['w'] = 0 
inc('wfk', -566) if registers['w'] <= 421 else do_nothing()
if registers['wfk'] > highest:
   highest = registers['wfk'] 
if 'nkr' not in registers.keys(): registers['nkr'] = 0 
if 'w' not in registers.keys(): registers['w'] = 0 
dec('nkr', 795) if registers['w'] < 426 else do_nothing()
if registers['nkr'] > highest:
   highest = registers['nkr'] 
if 'k' not in registers.keys(): registers['k'] = 0 
if 'sh' not in registers.keys(): registers['sh'] = 0 
dec('k', -372) if registers['sh'] <= -189 else do_nothing()
if registers['k'] > highest:
   highest = registers['k'] 
if 'lpi' not in registers.keys(): registers['lpi'] = 0 
if 't' not in registers.keys(): registers['t'] = 0 
inc('lpi', -167) if registers['t'] < -2137 else do_nothing()
if registers['lpi'] > highest:
   highest = registers['lpi'] 
if 'rlq' not in registers.keys(): registers['rlq'] = 0 
if 'qdq' not in registers.keys(): registers['qdq'] = 0 
dec('rlq', -939) if registers['qdq'] != 1522 else do_nothing()
if registers['rlq'] > highest:
   highest = registers['rlq'] 
if 'yo' not in registers.keys(): registers['yo'] = 0 
if 'jh' not in registers.keys(): registers['jh'] = 0 
dec('yo', 223) if registers['jh'] < -3439 else do_nothing()
if registers['yo'] > highest:
   highest = registers['yo'] 
if 'qrc' not in registers.keys(): registers['qrc'] = 0 
if 'ghj' not in registers.keys(): registers['ghj'] = 0 
dec('qrc', -151) if registers['ghj'] < 108 else do_nothing()
if registers['qrc'] > highest:
   highest = registers['qrc'] 
if 'fkp' not in registers.keys(): registers['fkp'] = 0 
if 'ev' not in registers.keys(): registers['ev'] = 0 
inc('fkp', 172) if registers['ev'] > 229 else do_nothing()
if registers['fkp'] > highest:
   highest = registers['fkp'] 
if 'qdq' not in registers.keys(): registers['qdq'] = 0 
if 'u' not in registers.keys(): registers['u'] = 0 
inc('qdq', -527) if registers['u'] == -1529 else do_nothing()
if registers['qdq'] > highest:
   highest = registers['qdq'] 
if 'u' not in registers.keys(): registers['u'] = 0 
if 'vh' not in registers.keys(): registers['vh'] = 0 
dec('u', -376) if registers['vh'] == -1763 else do_nothing()
if registers['u'] > highest:
   highest = registers['u'] 
if 'nkr' not in registers.keys(): registers['nkr'] = 0 
if 'u' not in registers.keys(): registers['u'] = 0 
inc('nkr', 201) if registers['u'] <= -1149 else do_nothing()
if registers['nkr'] > highest:
   highest = registers['nkr'] 
if 'qdq' not in registers.keys(): registers['qdq'] = 0 
if 'pr' not in registers.keys(): registers['pr'] = 0 
dec('qdq', -277) if registers['pr'] != -3595 else do_nothing()
if registers['qdq'] > highest:
   highest = registers['qdq'] 
if 'ghj' not in registers.keys(): registers['ghj'] = 0 
if 'qdq' not in registers.keys(): registers['qdq'] = 0 
dec('ghj', 560) if registers['qdq'] > 1256 else do_nothing()
if registers['ghj'] > highest:
   highest = registers['ghj'] 
if 'sh' not in registers.keys(): registers['sh'] = 0 
if 'jh' not in registers.keys(): registers['jh'] = 0 
inc('sh', -957) if registers['jh'] <= -3444 else do_nothing()
if registers['sh'] > highest:
   highest = registers['sh'] 
if 'a' not in registers.keys(): registers['a'] = 0 
if 'wfk' not in registers.keys(): registers['wfk'] = 0 
inc('a', 926) if registers['wfk'] >= 627 else do_nothing()
if registers['a'] > highest:
   highest = registers['a'] 
if 'pr' not in registers.keys(): registers['pr'] = 0 
if 'yo' not in registers.keys(): registers['yo'] = 0 
dec('pr', -156) if registers['yo'] < -1594 else do_nothing()
if registers['pr'] > highest:
   highest = registers['pr'] 
if 'rlq' not in registers.keys(): registers['rlq'] = 0 
if 't' not in registers.keys(): registers['t'] = 0 
inc('rlq', 942) if registers['t'] >= -2147 else do_nothing()
if registers['rlq'] > highest:
   highest = registers['rlq'] 
if 'qrc' not in registers.keys(): registers['qrc'] = 0 
if 'rlq' not in registers.keys(): registers['rlq'] = 0 
inc('qrc', -702) if registers['rlq'] != 1620 else do_nothing()
if registers['qrc'] > highest:
   highest = registers['qrc'] 
if 'qdq' not in registers.keys(): registers['qdq'] = 0 
if 'g' not in registers.keys(): registers['g'] = 0 
inc('qdq', -202) if registers['g'] >= -1550 else do_nothing()
if registers['qdq'] > highest:
   highest = registers['qdq'] 
if 'ghj' not in registers.keys(): registers['ghj'] = 0 
if 'fkp' not in registers.keys(): registers['fkp'] = 0 
dec('ghj', 939) if registers['fkp'] < 2320 else do_nothing()
if registers['ghj'] > highest:
   highest = registers['ghj'] 
if 'qdq' not in registers.keys(): registers['qdq'] = 0 
if 'jq' not in registers.keys(): registers['jq'] = 0 
dec('qdq', -990) if registers['jq'] == 2344 else do_nothing()
if registers['qdq'] > highest:
   highest = registers['qdq'] 
if 'vh' not in registers.keys(): registers['vh'] = 0 
if 'qdq' not in registers.keys(): registers['qdq'] = 0 
inc('vh', -584) if registers['qdq'] != 2262 else do_nothing()
if registers['vh'] > highest:
   highest = registers['vh'] 
if 'ev' not in registers.keys(): registers['ev'] = 0 
if 'wfk' not in registers.keys(): registers['wfk'] = 0 
dec('ev', 893) if registers['wfk'] >= 631 else do_nothing()
if registers['ev'] > highest:
   highest = registers['ev'] 
if 'pr' not in registers.keys(): registers['pr'] = 0 
if 'jh' not in registers.keys(): registers['jh'] = 0 
inc('pr', 441) if registers['jh'] <= -3444 else do_nothing()
if registers['pr'] > highest:
   highest = registers['pr'] 
if 'm' not in registers.keys(): registers['m'] = 0 
if 'fkp' not in registers.keys(): registers['fkp'] = 0 
inc('m', 262) if registers['fkp'] >= 2309 else do_nothing()
if registers['m'] > highest:
   highest = registers['m'] 
if 'k' not in registers.keys(): registers['k'] = 0 
if 'g' not in registers.keys(): registers['g'] = 0 
inc('k', 784) if registers['g'] == -1555 else do_nothing()
if registers['k'] > highest:
   highest = registers['k'] 
if 'jq' not in registers.keys(): registers['jq'] = 0 
if 'lpi' not in registers.keys(): registers['lpi'] = 0 
dec('jq', 425) if registers['lpi'] >= -520 else do_nothing()
if registers['jq'] > highest:
   highest = registers['jq'] 
if 'pr' not in registers.keys(): registers['pr'] = 0 
if 'qn' not in registers.keys(): registers['qn'] = 0 
dec('pr', 703) if registers['qn'] == 481 else do_nothing()
if registers['pr'] > highest:
   highest = registers['pr'] 
if 'afu' not in registers.keys(): registers['afu'] = 0 
if 'yo' not in registers.keys(): registers['yo'] = 0 
dec('afu', 380) if registers['yo'] < -1612 else do_nothing()
if registers['afu'] > highest:
   highest = registers['afu'] 
if 'qrc' not in registers.keys(): registers['qrc'] = 0 
if 'sh' not in registers.keys(): registers['sh'] = 0 
dec('qrc', 919) if registers['sh'] == -1148 else do_nothing()
if registers['qrc'] > highest:
   highest = registers['qrc'] 
if 'qdq' not in registers.keys(): registers['qdq'] = 0 
if 'jh' not in registers.keys(): registers['jh'] = 0 
inc('qdq', 148) if registers['jh'] != -3456 else do_nothing()
if registers['qdq'] > highest:
   highest = registers['qdq'] 
if 'k' not in registers.keys(): registers['k'] = 0 
if 'm' not in registers.keys(): registers['m'] = 0 
inc('k', -203) if registers['m'] >= 1425 else do_nothing()
if registers['k'] > highest:
   highest = registers['k'] 
if 'sh' not in registers.keys(): registers['sh'] = 0 
if 'qdq' not in registers.keys(): registers['qdq'] = 0 
dec('sh', -5) if registers['qdq'] >= 2403 else do_nothing()
if registers['sh'] > highest:
   highest = registers['sh'] 
if 'w' not in registers.keys(): registers['w'] = 0 
if 'pr' not in registers.keys(): registers['pr'] = 0 
dec('w', -310) if registers['pr'] < -2992 else do_nothing()
if registers['w'] > highest:
   highest = registers['w'] 
if 'u' not in registers.keys(): registers['u'] = 0 
if 'nkr' not in registers.keys(): registers['nkr'] = 0 
inc('u', -631) if registers['nkr'] > -2827 else do_nothing()
if registers['u'] > highest:
   highest = registers['u'] 
if 'fkp' not in registers.keys(): registers['fkp'] = 0 
if 'u' not in registers.keys(): registers['u'] = 0 
dec('fkp', 858) if registers['u'] <= -1789 else do_nothing()
if registers['fkp'] > highest:
   highest = registers['fkp'] 
if 'ev' not in registers.keys(): registers['ev'] = 0 
if 'wfk' not in registers.keys(): registers['wfk'] = 0 
dec('ev', 351) if registers['wfk'] != 636 else do_nothing()
if registers['ev'] > highest:
   highest = registers['ev'] 
if 'sh' not in registers.keys(): registers['sh'] = 0 
if 'ghj' not in registers.keys(): registers['ghj'] = 0 
inc('sh', 875) if registers['ghj'] >= -1400 else do_nothing()
if registers['sh'] > highest:
   highest = registers['sh'] 
if 'qn' not in registers.keys(): registers['qn'] = 0 
if 'qn' not in registers.keys(): registers['qn'] = 0 
inc('qn', 206) if registers['qn'] == 476 else do_nothing()
if registers['qn'] > highest:
   highest = registers['qn'] 
if 'pr' not in registers.keys(): registers['pr'] = 0 
if 'pr' not in registers.keys(): registers['pr'] = 0 
inc('pr', -973) if registers['pr'] >= -2988 else do_nothing()
if registers['pr'] > highest:
   highest = registers['pr'] 
if 'qrc' not in registers.keys(): registers['qrc'] = 0 
if 'a' not in registers.keys(): registers['a'] = 0 
inc('qrc', 267) if registers['a'] < -2315 else do_nothing()
if registers['qrc'] > highest:
   highest = registers['qrc'] 
if 'k' not in registers.keys(): registers['k'] = 0 
if 'lpi' not in registers.keys(): registers['lpi'] = 0 
inc('k', -176) if registers['lpi'] != -519 else do_nothing()
if registers['k'] > highest:
   highest = registers['k'] 
if 'g' not in registers.keys(): registers['g'] = 0 
if 'sh' not in registers.keys(): registers['sh'] = 0 
dec('g', -388) if registers['sh'] <= -267 else do_nothing()
if registers['g'] > highest:
   highest = registers['g'] 
if 'ghj' not in registers.keys(): registers['ghj'] = 0 
if 'lpi' not in registers.keys(): registers['lpi'] = 0 
dec('ghj', 706) if registers['lpi'] >= -516 else do_nothing()
if registers['ghj'] > highest:
   highest = registers['ghj'] 
if 'sh' not in registers.keys(): registers['sh'] = 0 
if 'rlq' not in registers.keys(): registers['rlq'] = 0 
dec('sh', -616) if registers['rlq'] == 1628 else do_nothing()
if registers['sh'] > highest:
   highest = registers['sh'] 
if 'fkp' not in registers.keys(): registers['fkp'] = 0 
if 'g' not in registers.keys(): registers['g'] = 0 
dec('fkp', 199) if registers['g'] < -1157 else do_nothing()
if registers['fkp'] > highest:
   highest = registers['fkp'] 
if 'qn' not in registers.keys(): registers['qn'] = 0 
if 'qn' not in registers.keys(): registers['qn'] = 0 
dec('qn', 749) if registers['qn'] > 687 else do_nothing()
if registers['qn'] > highest:
   highest = registers['qn'] 
if 'qn' not in registers.keys(): registers['qn'] = 0 
if 'wfk' not in registers.keys(): registers['wfk'] = 0 
inc('qn', -250) if registers['wfk'] == 634 else do_nothing()
if registers['qn'] > highest:
   highest = registers['qn'] 
if 'm' not in registers.keys(): registers['m'] = 0 
if 'qdq' not in registers.keys(): registers['qdq'] = 0 
dec('m', 4) if registers['qdq'] > 2398 else do_nothing()
if registers['m'] > highest:
   highest = registers['m'] 
if 't' not in registers.keys(): registers['t'] = 0 
if 'ev' not in registers.keys(): registers['ev'] = 0 
inc('t', 723) if registers['ev'] >= -1015 else do_nothing()
if registers['t'] > highest:
   highest = registers['t'] 
if 'w' not in registers.keys(): registers['w'] = 0 
if 'ev' not in registers.keys(): registers['ev'] = 0 
dec('w', 377) if registers['ev'] < -1006 else do_nothing()
if registers['w'] > highest:
   highest = registers['w'] 
if 'qdq' not in registers.keys(): registers['qdq'] = 0 
if 'sh' not in registers.keys(): registers['sh'] = 0 
inc('qdq', 662) if registers['sh'] > 340 else do_nothing()
if registers['qdq'] > highest:
   highest = registers['qdq'] 
if 'yo' not in registers.keys(): registers['yo'] = 0 
if 'ev' not in registers.keys(): registers['ev'] = 0 
inc('yo', 944) if registers['ev'] < -1011 else do_nothing()
if registers['yo'] > highest:
   highest = registers['yo'] 
if 'nkr' not in registers.keys(): registers['nkr'] = 0 
if 'bfx' not in registers.keys(): registers['bfx'] = 0 
inc('nkr', 625) if registers['bfx'] >= 1732 else do_nothing()
if registers['nkr'] > highest:
   highest = registers['nkr'] 
if 'bfx' not in registers.keys(): registers['bfx'] = 0 
if 'vh' not in registers.keys(): registers['vh'] = 0 
inc('bfx', 313) if registers['vh'] < -2350 else do_nothing()
if registers['bfx'] > highest:
   highest = registers['bfx'] 
if 'u' not in registers.keys(): registers['u'] = 0 
if 'ghj' not in registers.keys(): registers['ghj'] = 0 
inc('u', -675) if registers['ghj'] != -2098 else do_nothing()
if registers['u'] > highest:
   highest = registers['u'] 
if 'bfx' not in registers.keys(): registers['bfx'] = 0 
if 'vh' not in registers.keys(): registers['vh'] = 0 
dec('bfx', -228) if registers['vh'] >= -2349 else do_nothing()
if registers['bfx'] > highest:
   highest = registers['bfx'] 
if 'lpi' not in registers.keys(): registers['lpi'] = 0 
if 'ev' not in registers.keys(): registers['ev'] = 0 
inc('lpi', -269) if registers['ev'] > -1006 else do_nothing()
if registers['lpi'] > highest:
   highest = registers['lpi'] 
if 'qn' not in registers.keys(): registers['qn'] = 0 
if 'ghj' not in registers.keys(): registers['ghj'] = 0 
dec('qn', -264) if registers['ghj'] < -2091 else do_nothing()
if registers['qn'] > highest:
   highest = registers['qn'] 
if 'yo' not in registers.keys(): registers['yo'] = 0 
if 'vh' not in registers.keys(): registers['vh'] = 0 
inc('yo', -718) if registers['vh'] == -2347 else do_nothing()
if registers['yo'] > highest:
   highest = registers['yo'] 
if 'ghj' not in registers.keys(): registers['ghj'] = 0 
if 'k' not in registers.keys(): registers['k'] = 0 
dec('ghj', -646) if registers['k'] < 2276 else do_nothing()
if registers['ghj'] > highest:
   highest = registers['ghj'] 
if 'm' not in registers.keys(): registers['m'] = 0 
if 'u' not in registers.keys(): registers['u'] = 0 
inc('m', -541) if registers['u'] != -1793 else do_nothing()
if registers['m'] > highest:
   highest = registers['m'] 
if 'w' not in registers.keys(): registers['w'] = 0 
if 'jh' not in registers.keys(): registers['jh'] = 0 
inc('w', 809) if registers['jh'] >= -3456 else do_nothing()
if registers['w'] > highest:
   highest = registers['w'] 
if 'qrc' not in registers.keys(): registers['qrc'] = 0 
if 'jq' not in registers.keys(): registers['jq'] = 0 
dec('qrc', 962) if registers['jq'] <= 1912 else do_nothing()
if registers['qrc'] > highest:
   highest = registers['qrc'] 
if 'k' not in registers.keys(): registers['k'] = 0 
if 'lpi' not in registers.keys(): registers['lpi'] = 0 
dec('k', -908) if registers['lpi'] > -514 else do_nothing()
if registers['k'] > highest:
   highest = registers['k'] 
if 'g' not in registers.keys(): registers['g'] = 0 
if 'm' not in registers.keys(): registers['m'] = 0 
dec('g', -163) if registers['m'] < 884 else do_nothing()
if registers['g'] > highest:
   highest = registers['g'] 
if 'pr' not in registers.keys(): registers['pr'] = 0 
if 'vh' not in registers.keys(): registers['vh'] = 0 
inc('pr', -801) if registers['vh'] < -2338 else do_nothing()
if registers['pr'] > highest:
   highest = registers['pr'] 
if 'a' not in registers.keys(): registers['a'] = 0 
if 'vh' not in registers.keys(): registers['vh'] = 0 
inc('a', 958) if registers['vh'] < -2341 else do_nothing()
if registers['a'] > highest:
   highest = registers['a'] 
if 'fkp' not in registers.keys(): registers['fkp'] = 0 
if 'vh' not in registers.keys(): registers['vh'] = 0 
inc('fkp', 452) if registers['vh'] >= -2347 else do_nothing()
if registers['fkp'] > highest:
   highest = registers['fkp'] 
if 'nkr' not in registers.keys(): registers['nkr'] = 0 
if 'k' not in registers.keys(): registers['k'] = 0 
dec('nkr', -481) if registers['k'] < 3179 else do_nothing()
if registers['nkr'] > highest:
   highest = registers['nkr'] 
if 'g' not in registers.keys(): registers['g'] = 0 
if 'u' not in registers.keys(): registers['u'] = 0 
inc('g', 682) if registers['u'] >= -1778 else do_nothing()
if registers['g'] > highest:
   highest = registers['g'] 
if 'vh' not in registers.keys(): registers['vh'] = 0 
if 'bfx' not in registers.keys(): registers['bfx'] = 0 
dec('vh', -178) if registers['bfx'] >= 1968 else do_nothing()
if registers['vh'] > highest:
   highest = registers['vh'] 
if 'qn' not in registers.keys(): registers['qn'] = 0 
if 'qn' not in registers.keys(): registers['qn'] = 0 
dec('qn', -293) if registers['qn'] > 686 else do_nothing()
if registers['qn'] > highest:
   highest = registers['qn'] 
if 'sh' not in registers.keys(): registers['sh'] = 0 
if 'sh' not in registers.keys(): registers['sh'] = 0 
dec('sh', 612) if registers['sh'] != 352 else do_nothing()
if registers['sh'] > highest:
   highest = registers['sh'] 
if 'bfx' not in registers.keys(): registers['bfx'] = 0 
if 'lpi' not in registers.keys(): registers['lpi'] = 0 
dec('bfx', 473) if registers['lpi'] <= -505 else do_nothing()
if registers['bfx'] > highest:
   highest = registers['bfx'] 
if 'm' not in registers.keys(): registers['m'] = 0 
if 'a' not in registers.keys(): registers['a'] = 0 
dec('m', 77) if registers['a'] != -1376 else do_nothing()
if registers['m'] > highest:
   highest = registers['m'] 
if 'rlq' not in registers.keys(): registers['rlq'] = 0 
if 'qn' not in registers.keys(): registers['qn'] = 0 
dec('rlq', 709) if registers['qn'] != 987 else do_nothing()
if registers['rlq'] > highest:
   highest = registers['rlq'] 
if 'vh' not in registers.keys(): registers['vh'] = 0 
if 'qdq' not in registers.keys(): registers['qdq'] = 0 
inc('vh', -342) if registers['qdq'] >= 3068 else do_nothing()
if registers['vh'] > highest:
   highest = registers['vh'] 
if 'lpi' not in registers.keys(): registers['lpi'] = 0 
if 't' not in registers.keys(): registers['t'] = 0 
dec('lpi', -146) if registers['t'] <= -1416 else do_nothing()
if registers['lpi'] > highest:
   highest = registers['lpi'] 
if 'vh' not in registers.keys(): registers['vh'] = 0 
if 'nkr' not in registers.keys(): registers['nkr'] = 0 
inc('vh', 949) if registers['nkr'] >= -2209 else do_nothing()
if registers['vh'] > highest:
   highest = registers['vh'] 
if 'jh' not in registers.keys(): registers['jh'] = 0 
if 'rlq' not in registers.keys(): registers['rlq'] = 0 
dec('jh', -311) if registers['rlq'] < 926 else do_nothing()
if registers['jh'] > highest:
   highest = registers['jh'] 
if 'yo' not in registers.keys(): registers['yo'] = 0 
if 'qn' not in registers.keys(): registers['qn'] = 0 
dec('yo', 407) if registers['qn'] > 987 else do_nothing()
if registers['yo'] > highest:
   highest = registers['yo'] 
if 'qrc' not in registers.keys(): registers['qrc'] = 0 
if 'qdq' not in registers.keys(): registers['qdq'] = 0 
inc('qrc', -530) if registers['qdq'] != 3056 else do_nothing()
if registers['qrc'] > highest:
   highest = registers['qrc'] 
if 'lpi' not in registers.keys(): registers['lpi'] = 0 
if 'pr' not in registers.keys(): registers['pr'] = 0 
inc('lpi', -879) if registers['pr'] >= -3802 else do_nothing()
if registers['lpi'] > highest:
   highest = registers['lpi'] 
if 'qrc' not in registers.keys(): registers['qrc'] = 0 
if 'qn' not in registers.keys(): registers['qn'] = 0 
dec('qrc', -456) if registers['qn'] <= 987 else do_nothing()
if registers['qrc'] > highest:
   highest = registers['qrc'] 
if 't' not in registers.keys(): registers['t'] = 0 
if 'pr' not in registers.keys(): registers['pr'] = 0 
dec('t', -656) if registers['pr'] < -3785 else do_nothing()
if registers['t'] > highest:
   highest = registers['t'] 
if 'a' not in registers.keys(): registers['a'] = 0 
if 'wfk' not in registers.keys(): registers['wfk'] = 0 
dec('a', 382) if registers['wfk'] != 629 else do_nothing()
if registers['a'] > highest:
   highest = registers['a'] 
if 'pr' not in registers.keys(): registers['pr'] = 0 
if 'u' not in registers.keys(): registers['u'] = 0 
inc('pr', -873) if registers['u'] != -1790 else do_nothing()
if registers['pr'] > highest:
   highest = registers['pr'] 
if 'ev' not in registers.keys(): registers['ev'] = 0 
if 'wfk' not in registers.keys(): registers['wfk'] = 0 
dec('ev', -719) if registers['wfk'] >= 628 else do_nothing()
if registers['ev'] > highest:
   highest = registers['ev'] 
if 'qrc' not in registers.keys(): registers['qrc'] = 0 
if 'fkp' not in registers.keys(): registers['fkp'] = 0 
dec('qrc', -324) if registers['fkp'] > 2569 else do_nothing()
if registers['qrc'] > highest:
   highest = registers['qrc'] 
if 'g' not in registers.keys(): registers['g'] = 0 
if 'qrc' not in registers.keys(): registers['qrc'] = 0 
dec('g', -53) if registers['qrc'] >= -3892 else do_nothing()
if registers['g'] > highest:
   highest = registers['g'] 
if 'bfx' not in registers.keys(): registers['bfx'] = 0 
if 'ghj' not in registers.keys(): registers['ghj'] = 0 
inc('bfx', -869) if registers['ghj'] < -1446 else do_nothing()
if registers['bfx'] > highest:
   highest = registers['bfx'] 
if 'ev' not in registers.keys(): registers['ev'] = 0 
if 'a' not in registers.keys(): registers['a'] = 0 
dec('ev', 528) if registers['a'] < -1739 else do_nothing()
if registers['ev'] > highest:
   highest = registers['ev'] 
if 'sh' not in registers.keys(): registers['sh'] = 0 
if 'vh' not in registers.keys(): registers['vh'] = 0 
inc('sh', 260) if registers['vh'] <= -1402 else do_nothing()
if registers['sh'] > highest:
   highest = registers['sh'] 
if 'yo' not in registers.keys(): registers['yo'] = 0 
if 'afu' not in registers.keys(): registers['afu'] = 0 
inc('yo', -751) if registers['afu'] > 1354 else do_nothing()
if registers['yo'] > highest:
   highest = registers['yo'] 
if 'afu' not in registers.keys(): registers['afu'] = 0 
if 'pr' not in registers.keys(): registers['pr'] = 0 
inc('afu', -609) if registers['pr'] == -4667 else do_nothing()
if registers['afu'] > highest:
   highest = registers['afu'] 
if 'wfk' not in registers.keys(): registers['wfk'] = 0 
if 'm' not in registers.keys(): registers['m'] = 0 
inc('wfk', -413) if registers['m'] >= 798 else do_nothing()
if registers['wfk'] > highest:
   highest = registers['wfk'] 
if 'u' not in registers.keys(): registers['u'] = 0 
if 'lpi' not in registers.keys(): registers['lpi'] = 0 
inc('u', -701) if registers['lpi'] <= -1245 else do_nothing()
if registers['u'] > highest:
   highest = registers['u'] 
if 'ev' not in registers.keys(): registers['ev'] = 0 
if 'nkr' not in registers.keys(): registers['nkr'] = 0 
dec('ev', -712) if registers['nkr'] != -2205 else do_nothing()
if registers['ev'] > highest:
   highest = registers['ev'] 
if 'sh' not in registers.keys(): registers['sh'] = 0 
if 'fkp' not in registers.keys(): registers['fkp'] = 0 
dec('sh', 482) if registers['fkp'] != 2558 else do_nothing()
if registers['sh'] > highest:
   highest = registers['sh'] 
if 'nkr' not in registers.keys(): registers['nkr'] = 0 
if 'a' not in registers.keys(): registers['a'] = 0 
dec('nkr', -302) if registers['a'] >= -1753 else do_nothing()
if registers['nkr'] > highest:
   highest = registers['nkr'] 
if 'k' not in registers.keys(): registers['k'] = 0 
if 'm' not in registers.keys(): registers['m'] = 0 
inc('k', -354) if registers['m'] < 795 else do_nothing()
if registers['k'] > highest:
   highest = registers['k'] 
if 'bfx' not in registers.keys(): registers['bfx'] = 0 
if 'sh' not in registers.keys(): registers['sh'] = 0 
inc('bfx', 949) if registers['sh'] == -746 else do_nothing()
if registers['bfx'] > highest:
   highest = registers['bfx'] 
if 'lpi' not in registers.keys(): registers['lpi'] = 0 
if 'u' not in registers.keys(): registers['u'] = 0 
dec('lpi', 407) if registers['u'] <= -2480 else do_nothing()
if registers['lpi'] > highest:
   highest = registers['lpi'] 
if 'qn' not in registers.keys(): registers['qn'] = 0 
if 'pr' not in registers.keys(): registers['pr'] = 0 
dec('qn', -759) if registers['pr'] < -4666 else do_nothing()
if registers['qn'] > highest:
   highest = registers['qn'] 
if 'rlq' not in registers.keys(): registers['rlq'] = 0 
if 'afu' not in registers.keys(): registers['afu'] = 0 
dec('rlq', 118) if registers['afu'] > 733 else do_nothing()
if registers['rlq'] > highest:
   highest = registers['rlq'] 
if 'w' not in registers.keys(): registers['w'] = 0 
if 'g' not in registers.keys(): registers['g'] = 0 
inc('w', -978) if registers['g'] == -1004 else do_nothing()
if registers['w'] > highest:
   highest = registers['w'] 
if 'sh' not in registers.keys(): registers['sh'] = 0 
if 'qrc' not in registers.keys(): registers['qrc'] = 0 
inc('sh', -379) if registers['qrc'] != -3894 else do_nothing()
if registers['sh'] > highest:
   highest = registers['sh'] 
if 'a' not in registers.keys(): registers['a'] = 0 
if 'wfk' not in registers.keys(): registers['wfk'] = 0 
inc('a', 331) if registers['wfk'] > 213 else do_nothing()
if registers['a'] > highest:
   highest = registers['a'] 
if 'wfk' not in registers.keys(): registers['wfk'] = 0 
if 'bfx' not in registers.keys(): registers['bfx'] = 0 
dec('wfk', 476) if registers['bfx'] == 1567 else do_nothing()
if registers['wfk'] > highest:
   highest = registers['wfk'] 
if 'vh' not in registers.keys(): registers['vh'] = 0 
if 'qdq' not in registers.keys(): registers['qdq'] = 0 
dec('vh', 980) if registers['qdq'] > 3073 else do_nothing()
if registers['vh'] > highest:
   highest = registers['vh'] 
if 'jq' not in registers.keys(): registers['jq'] = 0 
if 'nkr' not in registers.keys(): registers['nkr'] = 0 
inc('jq', 596) if registers['nkr'] > -1901 else do_nothing()
if registers['jq'] > highest:
   highest = registers['jq'] 
if 'nkr' not in registers.keys(): registers['nkr'] = 0 
if 'fkp' not in registers.keys(): registers['fkp'] = 0 
inc('nkr', 142) if registers['fkp'] <= 2573 else do_nothing()
if registers['nkr'] > highest:
   highest = registers['nkr'] 
if 'yo' not in registers.keys(): registers['yo'] = 0 
if 'sh' not in registers.keys(): registers['sh'] = 0 
inc('yo', -343) if registers['sh'] >= -753 else do_nothing()
if registers['yo'] > highest:
   highest = registers['yo'] 
if 'bfx' not in registers.keys(): registers['bfx'] = 0 
if 'a' not in registers.keys(): registers['a'] = 0 
inc('bfx', 422) if registers['a'] != -1427 else do_nothing()
if registers['bfx'] > highest:
   highest = registers['bfx'] 
if 'a' not in registers.keys(): registers['a'] = 0 
if 'bfx' not in registers.keys(): registers['bfx'] = 0 
dec('a', -593) if registers['bfx'] <= 1994 else do_nothing()
if registers['a'] > highest:
   highest = registers['a'] 
if 'ghj' not in registers.keys(): registers['ghj'] = 0 
if 'qdq' not in registers.keys(): registers['qdq'] = 0 
dec('ghj', 674) if registers['qdq'] <= 3062 else do_nothing()
if registers['ghj'] > highest:
   highest = registers['ghj'] 
if 'ghj' not in registers.keys(): registers['ghj'] = 0 
if 'w' not in registers.keys(): registers['w'] = 0 
inc('ghj', -759) if registers['w'] > 172 else do_nothing()
if registers['ghj'] > highest:
   highest = registers['ghj'] 
if 'qn' not in registers.keys(): registers['qn'] = 0 
if 'qdq' not in registers.keys(): registers['qdq'] = 0 
dec('qn', -754) if registers['qdq'] >= 3060 else do_nothing()
if registers['qn'] > highest:
   highest = registers['qn'] 
if 'qdq' not in registers.keys(): registers['qdq'] = 0 
if 'qn' not in registers.keys(): registers['qn'] = 0 
dec('qdq', 971) if registers['qn'] <= 2507 else do_nothing()
if registers['qdq'] > highest:
   highest = registers['qdq'] 
if 'w' not in registers.keys(): registers['w'] = 0 
if 'nkr' not in registers.keys(): registers['nkr'] = 0 
inc('w', 183) if registers['nkr'] != -1756 else do_nothing()
if registers['w'] > highest:
   highest = registers['w'] 
if 'vh' not in registers.keys(): registers['vh'] = 0 
if 'jh' not in registers.keys(): registers['jh'] = 0 
dec('vh', 27) if registers['jh'] != -3145 else do_nothing()
if registers['vh'] > highest:
   highest = registers['vh'] 
if 'm' not in registers.keys(): registers['m'] = 0 
if 't' not in registers.keys(): registers['t'] = 0 
inc('m', -466) if registers['t'] < -758 else do_nothing()
if registers['m'] > highest:
   highest = registers['m'] 
if 'qdq' not in registers.keys(): registers['qdq'] = 0 
if 'u' not in registers.keys(): registers['u'] = 0 
inc('qdq', 28) if registers['u'] != -2477 else do_nothing()
if registers['qdq'] > highest:
   highest = registers['qdq'] 
if 'nkr' not in registers.keys(): registers['nkr'] = 0 
if 'qdq' not in registers.keys(): registers['qdq'] = 0 
inc('nkr', -676) if registers['qdq'] >= 2119 else do_nothing()
if registers['nkr'] > highest:
   highest = registers['nkr'] 
if 'jh' not in registers.keys(): registers['jh'] = 0 
if 'afu' not in registers.keys(): registers['afu'] = 0 
inc('jh', -701) if registers['afu'] >= 731 else do_nothing()
if registers['jh'] > highest:
   highest = registers['jh'] 
if 'bfx' not in registers.keys(): registers['bfx'] = 0 
if 'nkr' not in registers.keys(): registers['nkr'] = 0 
inc('bfx', -995) if registers['nkr'] < -2432 else do_nothing()
if registers['bfx'] > highest:
   highest = registers['bfx'] 
if 'vh' not in registers.keys(): registers['vh'] = 0 
if 'sh' not in registers.keys(): registers['sh'] = 0 
inc('vh', -211) if registers['sh'] == -746 else do_nothing()
if registers['vh'] > highest:
   highest = registers['vh'] 
if 'pr' not in registers.keys(): registers['pr'] = 0 
if 'lpi' not in registers.keys(): registers['lpi'] = 0 
dec('pr', 896) if registers['lpi'] > -1659 else do_nothing()
if registers['pr'] > highest:
   highest = registers['pr'] 
if 'sh' not in registers.keys(): registers['sh'] = 0 
if 'pr' not in registers.keys(): registers['pr'] = 0 
dec('sh', 259) if registers['pr'] > -5568 else do_nothing()
if registers['sh'] > highest:
   highest = registers['sh'] 
if 'm' not in registers.keys(): registers['m'] = 0 
if 'fkp' not in registers.keys(): registers['fkp'] = 0 
dec('m', 138) if registers['fkp'] <= 2566 else do_nothing()
if registers['m'] > highest:
   highest = registers['m'] 
if 'g' not in registers.keys(): registers['g'] = 0 
if 'qrc' not in registers.keys(): registers['qrc'] = 0 
dec('g', 420) if registers['qrc'] <= -3888 else do_nothing()
if registers['g'] > highest:
   highest = registers['g'] 
if 'vh' not in registers.keys(): registers['vh'] = 0 
if 'yo' not in registers.keys(): registers['yo'] = 0 
inc('vh', 840) if registers['yo'] > -3074 else do_nothing()
if registers['vh'] > highest:
   highest = registers['vh'] 
if 'nkr' not in registers.keys(): registers['nkr'] = 0 
if 'a' not in registers.keys(): registers['a'] = 0 
dec('nkr', 642) if registers['a'] <= -824 else do_nothing()
if registers['nkr'] > highest:
   highest = registers['nkr'] 
if 'nkr' not in registers.keys(): registers['nkr'] = 0 
if 'w' not in registers.keys(): registers['w'] = 0 
inc('nkr', 524) if registers['w'] >= 359 else do_nothing()
if registers['nkr'] > highest:
   highest = registers['nkr'] 
if 'ghj' not in registers.keys(): registers['ghj'] = 0 
if 'wfk' not in registers.keys(): registers['wfk'] = 0 
dec('ghj', -992) if registers['wfk'] == -255 else do_nothing()
if registers['ghj'] > highest:
   highest = registers['ghj'] 
if 'qrc' not in registers.keys(): registers['qrc'] = 0 
if 'vh' not in registers.keys(): registers['vh'] = 0 
dec('qrc', -75) if registers['vh'] == -796 else do_nothing()
if registers['qrc'] > highest:
   highest = registers['qrc'] 
if 'bfx' not in registers.keys(): registers['bfx'] = 0 
if 'g' not in registers.keys(): registers['g'] = 0 
inc('bfx', 1000) if registers['g'] < -1423 else do_nothing()
if registers['bfx'] > highest:
   highest = registers['bfx'] 
if 'g' not in registers.keys(): registers['g'] = 0 
if 'a' not in registers.keys(): registers['a'] = 0 
dec('g', -716) if registers['a'] >= -819 else do_nothing()
if registers['g'] > highest:
   highest = registers['g'] 
if 'nkr' not in registers.keys(): registers['nkr'] = 0 
if 'sh' not in registers.keys(): registers['sh'] = 0 
inc('nkr', -806) if registers['sh'] != -999 else do_nothing()
if registers['nkr'] > highest:
   highest = registers['nkr'] 
if 'pr' not in registers.keys(): registers['pr'] = 0 
if 'yo' not in registers.keys(): registers['yo'] = 0 
inc('pr', 83) if registers['yo'] < -3062 else do_nothing()
if registers['pr'] > highest:
   highest = registers['pr'] 
if 'pr' not in registers.keys(): registers['pr'] = 0 
if 'g' not in registers.keys(): registers['g'] = 0 
dec('pr', 231) if registers['g'] != -1424 else do_nothing()
if registers['pr'] > highest:
   highest = registers['pr'] 
if 'vh' not in registers.keys(): registers['vh'] = 0 
if 'lpi' not in registers.keys(): registers['lpi'] = 0 
inc('vh', 99) if registers['lpi'] <= -1651 else do_nothing()
if registers['vh'] > highest:
   highest = registers['vh'] 
if 'u' not in registers.keys(): registers['u'] = 0 
if 't' not in registers.keys(): registers['t'] = 0 
inc('u', -294) if registers['t'] <= -759 else do_nothing()
if registers['u'] > highest:
   highest = registers['u'] 
if 'fkp' not in registers.keys(): registers['fkp'] = 0 
if 'wfk' not in registers.keys(): registers['wfk'] = 0 
inc('fkp', -163) if registers['wfk'] < -245 else do_nothing()
if registers['fkp'] > highest:
   highest = registers['fkp'] 
if 'k' not in registers.keys(): registers['k'] = 0 
if 'afu' not in registers.keys(): registers['afu'] = 0 
inc('k', -221) if registers['afu'] == 727 else do_nothing()
if registers['k'] > highest:
   highest = registers['k'] 
if 'w' not in registers.keys(): registers['w'] = 0 
if 'qn' not in registers.keys(): registers['qn'] = 0 
dec('w', -661) if registers['qn'] == 2502 else do_nothing()
if registers['w'] > highest:
   highest = registers['w'] 
if 'ev' not in registers.keys(): registers['ev'] = 0 
if 'nkr' not in registers.keys(): registers['nkr'] = 0 
inc('ev', -892) if registers['nkr'] > -3364 else do_nothing()
if registers['ev'] > highest:
   highest = registers['ev'] 
if 'fkp' not in registers.keys(): registers['fkp'] = 0 
if 'g' not in registers.keys(): registers['g'] = 0 
inc('fkp', -224) if registers['g'] != -1434 else do_nothing()
if registers['fkp'] > highest:
   highest = registers['fkp'] 
if 'fkp' not in registers.keys(): registers['fkp'] = 0 
if 't' not in registers.keys(): registers['t'] = 0 
inc('fkp', -517) if registers['t'] > -752 else do_nothing()
if registers['fkp'] > highest:
   highest = registers['fkp'] 
if 'sh' not in registers.keys(): registers['sh'] = 0 
if 'qrc' not in registers.keys(): registers['qrc'] = 0 
dec('sh', 268) if registers['qrc'] != -3811 else do_nothing()
if registers['sh'] > highest:
   highest = registers['sh'] 
if 'sh' not in registers.keys(): registers['sh'] = 0 
if 'bfx' not in registers.keys(): registers['bfx'] = 0 
inc('sh', 907) if registers['bfx'] == 1994 else do_nothing()
if registers['sh'] > highest:
   highest = registers['sh'] 
if 'sh' not in registers.keys(): registers['sh'] = 0 
if 'afu' not in registers.keys(): registers['afu'] = 0 
inc('sh', -441) if registers['afu'] > 728 else do_nothing()
if registers['sh'] > highest:
   highest = registers['sh'] 
if 'yo' not in registers.keys(): registers['yo'] = 0 
if 'fkp' not in registers.keys(): registers['fkp'] = 0 
inc('yo', 81) if registers['fkp'] == 2176 else do_nothing()
if registers['yo'] > highest:
   highest = registers['yo'] 
if 'lpi' not in registers.keys(): registers['lpi'] = 0 
if 'ghj' not in registers.keys(): registers['ghj'] = 0 
inc('lpi', -280) if registers['ghj'] >= -1227 else do_nothing()
if registers['lpi'] > highest:
   highest = registers['lpi'] 
if 'qdq' not in registers.keys(): registers['qdq'] = 0 
if 'ev' not in registers.keys(): registers['ev'] = 0 
inc('qdq', -133) if registers['ev'] > -1000 else do_nothing()
if registers['qdq'] > highest:
   highest = registers['qdq'] 
if 'afu' not in registers.keys(): registers['afu'] = 0 
if 'fkp' not in registers.keys(): registers['fkp'] = 0 
dec('afu', -91) if registers['fkp'] == 2180 else do_nothing()
if registers['afu'] > highest:
   highest = registers['afu'] 
if 'qn' not in registers.keys(): registers['qn'] = 0 
if 'k' not in registers.keys(): registers['k'] = 0 
inc('qn', 513) if registers['k'] <= 3191 else do_nothing()
if registers['qn'] > highest:
   highest = registers['qn'] 
if 'u' not in registers.keys(): registers['u'] = 0 
if 'bfx' not in registers.keys(): registers['bfx'] = 0 
dec('u', -441) if registers['bfx'] == 1994 else do_nothing()
if registers['u'] > highest:
   highest = registers['u'] 
if 'm' not in registers.keys(): registers['m'] = 0 
if 'qdq' not in registers.keys(): registers['qdq'] = 0 
dec('m', 294) if registers['qdq'] > 2113 else do_nothing()
if registers['m'] > highest:
   highest = registers['m'] 
if 'w' not in registers.keys(): registers['w'] = 0 
if 'ev' not in registers.keys(): registers['ev'] = 0 
inc('w', 43) if registers['ev'] > -1004 else do_nothing()
if registers['w'] > highest:
   highest = registers['w'] 
if 'w' not in registers.keys(): registers['w'] = 0 
if 'ev' not in registers.keys(): registers['ev'] = 0 
inc('w', 742) if registers['ev'] > -998 else do_nothing()
if registers['w'] > highest:
   highest = registers['w'] 
if 'ev' not in registers.keys(): registers['ev'] = 0 
if 'rlq' not in registers.keys(): registers['rlq'] = 0 
inc('ev', -574) if registers['rlq'] > 801 else do_nothing()
if registers['ev'] > highest:
   highest = registers['ev'] 
if 'wfk' not in registers.keys(): registers['wfk'] = 0 
if 'qdq' not in registers.keys(): registers['qdq'] = 0 
dec('wfk', 811) if registers['qdq'] <= 2127 else do_nothing()
if registers['wfk'] > highest:
   highest = registers['wfk'] 
if 'bfx' not in registers.keys(): registers['bfx'] = 0 
if 'nkr' not in registers.keys(): registers['nkr'] = 0 
dec('bfx', -710) if registers['nkr'] <= -3349 else do_nothing()
if registers['bfx'] > highest:
   highest = registers['bfx'] 
if 'jh' not in registers.keys(): registers['jh'] = 0 
if 'lpi' not in registers.keys(): registers['lpi'] = 0 
inc('jh', -249) if registers['lpi'] < -1933 else do_nothing()
if registers['jh'] > highest:
   highest = registers['jh'] 
if 'jh' not in registers.keys(): registers['jh'] = 0 
if 'jq' not in registers.keys(): registers['jq'] = 0 
inc('jh', 471) if registers['jq'] >= 2506 else do_nothing()
if registers['jh'] > highest:
   highest = registers['jh'] 
if 'ev' not in registers.keys(): registers['ev'] = 0 
if 'qdq' not in registers.keys(): registers['qdq'] = 0 
inc('ev', 172) if registers['qdq'] > 2118 else do_nothing()
if registers['ev'] > highest:
   highest = registers['ev'] 
if 'm' not in registers.keys(): registers['m'] = 0 
if 'qrc' not in registers.keys(): registers['qrc'] = 0 
dec('m', 7) if registers['qrc'] >= -3811 else do_nothing()
if registers['m'] > highest:
   highest = registers['m'] 
if 'u' not in registers.keys(): registers['u'] = 0 
if 'afu' not in registers.keys(): registers['afu'] = 0 
inc('u', 409) if registers['afu'] > 823 else do_nothing()
if registers['u'] > highest:
   highest = registers['u'] 
if 'qn' not in registers.keys(): registers['qn'] = 0 
if 'qrc' not in registers.keys(): registers['qrc'] = 0 
dec('qn', 320) if registers['qrc'] < -3820 else do_nothing()
if registers['qn'] > highest:
   highest = registers['qn'] 
if 'vh' not in registers.keys(): registers['vh'] = 0 
if 'g' not in registers.keys(): registers['g'] = 0 
inc('vh', 861) if registers['g'] == -1424 else do_nothing()
if registers['vh'] > highest:
   highest = registers['vh'] 
if 'pr' not in registers.keys(): registers['pr'] = 0 
if 'ev' not in registers.keys(): registers['ev'] = 0 
inc('pr', 303) if registers['ev'] > -830 else do_nothing()
if registers['pr'] > highest:
   highest = registers['pr'] 
if 'vh' not in registers.keys(): registers['vh'] = 0 
if 'sh' not in registers.keys(): registers['sh'] = 0 
inc('vh', 939) if registers['sh'] < -810 else do_nothing()
if registers['vh'] > highest:
   highest = registers['vh'] 
if 'a' not in registers.keys(): registers['a'] = 0 
if 'a' not in registers.keys(): registers['a'] = 0 
dec('a', 903) if registers['a'] >= -815 else do_nothing()
if registers['a'] > highest:
   highest = registers['a'] 
if 'jq' not in registers.keys(): registers['jq'] = 0 
if 'sh' not in registers.keys(): registers['sh'] = 0 
inc('jq', 933) if registers['sh'] != -815 else do_nothing()
if registers['jq'] > highest:
   highest = registers['jq'] 
if 'qn' not in registers.keys(): registers['qn'] = 0 
if 'k' not in registers.keys(): registers['k'] = 0 
inc('qn', 614) if registers['k'] != 3188 else do_nothing()
if registers['qn'] > highest:
   highest = registers['qn'] 
if 'ev' not in registers.keys(): registers['ev'] = 0 
if 'jh' not in registers.keys(): registers['jh'] = 0 
dec('ev', 864) if registers['jh'] == -3367 else do_nothing()
if registers['ev'] > highest:
   highest = registers['ev'] 
if 'jh' not in registers.keys(): registers['jh'] = 0 
if 'rlq' not in registers.keys(): registers['rlq'] = 0 
dec('jh', -590) if registers['rlq'] == 801 else do_nothing()
if registers['jh'] > highest:
   highest = registers['jh'] 
if 'yo' not in registers.keys(): registers['yo'] = 0 
if 'u' not in registers.keys(): registers['u'] = 0 
dec('yo', 115) if registers['u'] != -1924 else do_nothing()
if registers['yo'] > highest:
   highest = registers['yo'] 
if 'wfk' not in registers.keys(): registers['wfk'] = 0 
if 'm' not in registers.keys(): registers['m'] = 0 
dec('wfk', 254) if registers['m'] == 41 else do_nothing()
if registers['wfk'] > highest:
   highest = registers['wfk'] 
if 'sh' not in registers.keys(): registers['sh'] = 0 
if 'fkp' not in registers.keys(): registers['fkp'] = 0 
dec('sh', 259) if registers['fkp'] >= 2171 else do_nothing()
if registers['sh'] > highest:
   highest = registers['sh'] 
if 'ghj' not in registers.keys(): registers['ghj'] = 0 
if 'bfx' not in registers.keys(): registers['bfx'] = 0 
inc('ghj', 571) if registers['bfx'] <= 2704 else do_nothing()
if registers['ghj'] > highest:
   highest = registers['ghj'] 
if 'ghj' not in registers.keys(): registers['ghj'] = 0 
if 'g' not in registers.keys(): registers['g'] = 0 
dec('ghj', 128) if registers['g'] == -1424 else do_nothing()
if registers['ghj'] > highest:
   highest = registers['ghj'] 
if 'k' not in registers.keys(): registers['k'] = 0 
if 'bfx' not in registers.keys(): registers['bfx'] = 0 
dec('k', 462) if registers['bfx'] != 2704 else do_nothing()
if registers['k'] > highest:
   highest = registers['k'] 
if 'nkr' not in registers.keys(): registers['nkr'] = 0 
if 'w' not in registers.keys(): registers['w'] = 0 
inc('nkr', 874) if registers['w'] <= 1076 else do_nothing()
if registers['nkr'] > highest:
   highest = registers['nkr'] 
if 'qrc' not in registers.keys(): registers['qrc'] = 0 
if 'ghj' not in registers.keys(): registers['ghj'] = 0 
inc('qrc', -180) if registers['ghj'] == -776 else do_nothing()
if registers['qrc'] > highest:
   highest = registers['qrc'] 
if 'qn' not in registers.keys(): registers['qn'] = 0 
if 'rlq' not in registers.keys(): registers['rlq'] = 0 
inc('qn', 812) if registers['rlq'] == 801 else do_nothing()
if registers['qn'] > highest:
   highest = registers['qn'] 
if 'afu' not in registers.keys(): registers['afu'] = 0 
if 'qn' not in registers.keys(): registers['qn'] = 0 
inc('afu', 297) if registers['qn'] >= 4437 else do_nothing()
if registers['afu'] > highest:
   highest = registers['afu'] 
if 'wfk' not in registers.keys(): registers['wfk'] = 0 
if 'pr' not in registers.keys(): registers['pr'] = 0 
dec('wfk', 497) if registers['pr'] >= -5170 else do_nothing()
if registers['wfk'] > highest:
   highest = registers['wfk'] 
if 'ghj' not in registers.keys(): registers['ghj'] = 0 
if 'vh' not in registers.keys(): registers['vh'] = 0 
dec('ghj', -805) if registers['vh'] == 169 else do_nothing()
if registers['ghj'] > highest:
   highest = registers['ghj'] 
if 'sh' not in registers.keys(): registers['sh'] = 0 
if 'bfx' not in registers.keys(): registers['bfx'] = 0 
inc('sh', 655) if registers['bfx'] == 2704 else do_nothing()
if registers['sh'] > highest:
   highest = registers['sh'] 
if 'lpi' not in registers.keys(): registers['lpi'] = 0 
if 'nkr' not in registers.keys(): registers['nkr'] = 0 
dec('lpi', -494) if registers['nkr'] < -2476 else do_nothing()
if registers['lpi'] > highest:
   highest = registers['lpi'] 
if 'nkr' not in registers.keys(): registers['nkr'] = 0 
if 'pr' not in registers.keys(): registers['pr'] = 0 
dec('nkr', -53) if registers['pr'] > -5181 else do_nothing()
if registers['nkr'] > highest:
   highest = registers['nkr'] 
if 'jq' not in registers.keys(): registers['jq'] = 0 
if 'nkr' not in registers.keys(): registers['nkr'] = 0 
dec('jq', -486) if registers['nkr'] == -2430 else do_nothing()
if registers['jq'] > highest:
   highest = registers['jq'] 
if 'vh' not in registers.keys(): registers['vh'] = 0 
if 'sh' not in registers.keys(): registers['sh'] = 0 
dec('vh', 708) if registers['sh'] <= -407 else do_nothing()
if registers['vh'] > highest:
   highest = registers['vh'] 
if 'fkp' not in registers.keys(): registers['fkp'] = 0 
if 'k' not in registers.keys(): registers['k'] = 0 
dec('fkp', -260) if registers['k'] == 3183 else do_nothing()
if registers['fkp'] > highest:
   highest = registers['fkp'] 
if 'rlq' not in registers.keys(): registers['rlq'] = 0 
if 'g' not in registers.keys(): registers['g'] = 0 
dec('rlq', -629) if registers['g'] == -1429 else do_nothing()
if registers['rlq'] > highest:
   highest = registers['rlq'] 
if 'nkr' not in registers.keys(): registers['nkr'] = 0 
if 'm' not in registers.keys(): registers['m'] = 0 
inc('nkr', -863) if registers['m'] == 41 else do_nothing()
if registers['nkr'] > highest:
   highest = registers['nkr'] 
if 'k' not in registers.keys(): registers['k'] = 0 
if 'k' not in registers.keys(): registers['k'] = 0 
inc('k', 897) if registers['k'] >= 3180 else do_nothing()
if registers['k'] > highest:
   highest = registers['k'] 
if 'u' not in registers.keys(): registers['u'] = 0 
if 'afu' not in registers.keys(): registers['afu'] = 0 
dec('u', -471) if registers['afu'] >= 1122 else do_nothing()
if registers['u'] > highest:
   highest = registers['u'] 
if 'yo' not in registers.keys(): registers['yo'] = 0 
if 'afu' not in registers.keys(): registers['afu'] = 0 
dec('yo', 460) if registers['afu'] != 1134 else do_nothing()
if registers['yo'] > highest:
   highest = registers['yo'] 
if 'ghj' not in registers.keys(): registers['ghj'] = 0 
if 'k' not in registers.keys(): registers['k'] = 0 
inc('ghj', 211) if registers['k'] > 4073 else do_nothing()
if registers['ghj'] > highest:
   highest = registers['ghj'] 
if 'jq' not in registers.keys(): registers['jq'] = 0 
if 'vh' not in registers.keys(): registers['vh'] = 0 
dec('jq', -10) if registers['vh'] < -535 else do_nothing()
if registers['jq'] > highest:
   highest = registers['jq'] 
if 'afu' not in registers.keys(): registers['afu'] = 0 
if 'pr' not in registers.keys(): registers['pr'] = 0 
inc('afu', -526) if registers['pr'] != -5167 else do_nothing()
if registers['afu'] > highest:
   highest = registers['afu'] 
if 'qdq' not in registers.keys(): registers['qdq'] = 0 
if 'wfk' not in registers.keys(): registers['wfk'] = 0 
inc('qdq', 399) if registers['wfk'] != -1319 else do_nothing()
if registers['qdq'] > highest:
   highest = registers['qdq'] 
if 'rlq' not in registers.keys(): registers['rlq'] = 0 
if 't' not in registers.keys(): registers['t'] = 0 
dec('rlq', 426) if registers['t'] < -757 else do_nothing()
if registers['rlq'] > highest:
   highest = registers['rlq'] 
if 'ev' not in registers.keys(): registers['ev'] = 0 
if 'bfx' not in registers.keys(): registers['bfx'] = 0 
inc('ev', -292) if registers['bfx'] == 2698 else do_nothing()
if registers['ev'] > highest:
   highest = registers['ev'] 
if 'vh' not in registers.keys(): registers['vh'] = 0 
if 'qdq' not in registers.keys(): registers['qdq'] = 0 
inc('vh', -345) if registers['qdq'] <= 2513 else do_nothing()
if registers['vh'] > highest:
   highest = registers['vh'] 
if 'jq' not in registers.keys(): registers['jq'] = 0 
if 'k' not in registers.keys(): registers['k'] = 0 
dec('jq', -722) if registers['k'] != 4083 else do_nothing()
if registers['jq'] > highest:
   highest = registers['jq'] 
if 'w' not in registers.keys(): registers['w'] = 0 
if 'sh' not in registers.keys(): registers['sh'] = 0 
dec('w', -15) if registers['sh'] == -411 else do_nothing()
if registers['w'] > highest:
   highest = registers['w'] 
if 'm' not in registers.keys(): registers['m'] = 0 
if 'lpi' not in registers.keys(): registers['lpi'] = 0 
dec('m', -191) if registers['lpi'] == -1439 else do_nothing()
if registers['m'] > highest:
   highest = registers['m'] 
if 't' not in registers.keys(): registers['t'] = 0 
if 'jh' not in registers.keys(): registers['jh'] = 0 
inc('t', -72) if registers['jh'] >= -2780 else do_nothing()
if registers['t'] > highest:
   highest = registers['t'] 
if 'sh' not in registers.keys(): registers['sh'] = 0 
if 'jh' not in registers.keys(): registers['jh'] = 0 
inc('sh', -664) if registers['jh'] != -2777 else do_nothing()
if registers['sh'] > highest:
   highest = registers['sh'] 
if 'lpi' not in registers.keys(): registers['lpi'] = 0 
if 'jh' not in registers.keys(): registers['jh'] = 0 
inc('lpi', 647) if registers['jh'] > -2784 else do_nothing()
if registers['lpi'] > highest:
   highest = registers['lpi'] 
if 'k' not in registers.keys(): registers['k'] = 0 
if 'afu' not in registers.keys(): registers['afu'] = 0 
inc('k', -651) if registers['afu'] == 599 else do_nothing()
if registers['k'] > highest:
   highest = registers['k'] 
if 'a' not in registers.keys(): registers['a'] = 0 
if 'nkr' not in registers.keys(): registers['nkr'] = 0 
inc('a', -431) if registers['nkr'] < -3287 else do_nothing()
if registers['a'] > highest:
   highest = registers['a'] 
if 'pr' not in registers.keys(): registers['pr'] = 0 
if 'g' not in registers.keys(): registers['g'] = 0 
dec('pr', 254) if registers['g'] <= -1418 else do_nothing()
if registers['pr'] > highest:
   highest = registers['pr'] 
if 'bfx' not in registers.keys(): registers['bfx'] = 0 
if 'ev' not in registers.keys(): registers['ev'] = 0 
inc('bfx', 288) if registers['ev'] >= -1683 else do_nothing()
if registers['bfx'] > highest:
   highest = registers['bfx'] 
if 'jh' not in registers.keys(): registers['jh'] = 0 
if 'wfk' not in registers.keys(): registers['wfk'] = 0 
inc('jh', -473) if registers['wfk'] < -1327 else do_nothing()
if registers['jh'] > highest:
   highest = registers['jh'] 
if 'jq' not in registers.keys(): registers['jq'] = 0 
if 'qdq' not in registers.keys(): registers['qdq'] = 0 
dec('jq', 871) if registers['qdq'] < 2529 else do_nothing()
if registers['jq'] > highest:
   highest = registers['jq'] 
if 'jq' not in registers.keys(): registers['jq'] = 0 
if 'bfx' not in registers.keys(): registers['bfx'] = 0 
dec('jq', 206) if registers['bfx'] < 2709 else do_nothing()
if registers['jq'] > highest:
   highest = registers['jq'] 
if 'm' not in registers.keys(): registers['m'] = 0 
if 'vh' not in registers.keys(): registers['vh'] = 0 
inc('m', 829) if registers['vh'] <= -535 else do_nothing()
if registers['m'] > highest:
   highest = registers['m'] 
if 'qrc' not in registers.keys(): registers['qrc'] = 0 
if 'qrc' not in registers.keys(): registers['qrc'] = 0 
dec('qrc', 412) if registers['qrc'] <= -3995 else do_nothing()
if registers['qrc'] > highest:
   highest = registers['qrc'] 
if 'g' not in registers.keys(): registers['g'] = 0 
if 'wfk' not in registers.keys(): registers['wfk'] = 0 
dec('g', -881) if registers['wfk'] > -1323 else do_nothing()
if registers['g'] > highest:
   highest = registers['g'] 
if 'qn' not in registers.keys(): registers['qn'] = 0 
if 'u' not in registers.keys(): registers['u'] = 0 
dec('qn', -999) if registers['u'] >= -1448 else do_nothing()
if registers['qn'] > highest:
   highest = registers['qn'] 
if 'ghj' not in registers.keys(): registers['ghj'] = 0 
if 'u' not in registers.keys(): registers['u'] = 0 
inc('ghj', -807) if registers['u'] >= -1459 else do_nothing()
if registers['ghj'] > highest:
   highest = registers['ghj'] 
if 'rlq' not in registers.keys(): registers['rlq'] = 0 
if 'sh' not in registers.keys(): registers['sh'] = 0 
dec('rlq', -967) if registers['sh'] > -421 else do_nothing()
if registers['rlq'] > highest:
   highest = registers['rlq'] 
if 'rlq' not in registers.keys(): registers['rlq'] = 0 
if 'vh' not in registers.keys(): registers['vh'] = 0 
inc('rlq', -608) if registers['vh'] < -536 else do_nothing()
if registers['rlq'] > highest:
   highest = registers['rlq'] 
if 't' not in registers.keys(): registers['t'] = 0 
if 'bfx' not in registers.keys(): registers['bfx'] = 0 
inc('t', -686) if registers['bfx'] != 2702 else do_nothing()
if registers['t'] > highest:
   highest = registers['t'] 
if 'yo' not in registers.keys(): registers['yo'] = 0 
if 't' not in registers.keys(): registers['t'] = 0 
inc('yo', -228) if registers['t'] >= -1520 else do_nothing()
if registers['yo'] > highest:
   highest = registers['yo'] 
if 'a' not in registers.keys(): registers['a'] = 0 
if 'afu' not in registers.keys(): registers['afu'] = 0 
inc('a', 650) if registers['afu'] > 597 else do_nothing()
if registers['a'] > highest:
   highest = registers['a'] 
if 'sh' not in registers.keys(): registers['sh'] = 0 
if 'fkp' not in registers.keys(): registers['fkp'] = 0 
dec('sh', -918) if registers['fkp'] > 2436 else do_nothing()
if registers['sh'] > highest:
   highest = registers['sh'] 
if 'm' not in registers.keys(): registers['m'] = 0 
if 'jq' not in registers.keys(): registers['jq'] = 0 
inc('m', 210) if registers['jq'] == 3589 else do_nothing()
if registers['m'] > highest:
   highest = registers['m'] 
if 'wfk' not in registers.keys(): registers['wfk'] = 0 
if 'vh' not in registers.keys(): registers['vh'] = 0 
dec('wfk', -634) if registers['vh'] > -535 else do_nothing()
if registers['wfk'] > highest:
   highest = registers['wfk'] 
if 't' not in registers.keys(): registers['t'] = 0 
if 'pr' not in registers.keys(): registers['pr'] = 0 
inc('t', -360) if registers['pr'] < -5427 else do_nothing()
if registers['t'] > highest:
   highest = registers['t'] 
if 'm' not in registers.keys(): registers['m'] = 0 
if 'k' not in registers.keys(): registers['k'] = 0 
inc('m', 899) if registers['k'] > 3424 else do_nothing()
if registers['m'] > highest:
   highest = registers['m'] 
if 'afu' not in registers.keys(): registers['afu'] = 0 
if 'jq' not in registers.keys(): registers['jq'] = 0 
dec('afu', -768) if registers['jq'] < 3594 else do_nothing()
if registers['afu'] > highest:
   highest = registers['afu'] 
if 'rlq' not in registers.keys(): registers['rlq'] = 0 
if 'ghj' not in registers.keys(): registers['ghj'] = 0 
inc('rlq', -990) if registers['ghj'] == -1372 else do_nothing()
if registers['rlq'] > highest:
   highest = registers['rlq'] 
if 't' not in registers.keys(): registers['t'] = 0 
if 'pr' not in registers.keys(): registers['pr'] = 0 
inc('t', -859) if registers['pr'] < -5438 else do_nothing()
if registers['t'] > highest:
   highest = registers['t'] 
if 'lpi' not in registers.keys(): registers['lpi'] = 0 
if 'jq' not in registers.keys(): registers['jq'] = 0 
inc('lpi', -961) if registers['jq'] == 3589 else do_nothing()
if registers['lpi'] > highest:
   highest = registers['lpi'] 
if 'bfx' not in registers.keys(): registers['bfx'] = 0 
if 'rlq' not in registers.keys(): registers['rlq'] = 0 
dec('bfx', -476) if registers['rlq'] != -248 else do_nothing()
if registers['bfx'] > highest:
   highest = registers['bfx'] 
if 'lpi' not in registers.keys(): registers['lpi'] = 0 
if 'ev' not in registers.keys(): registers['ev'] = 0 
dec('lpi', -238) if registers['ev'] > -1697 else do_nothing()
if registers['lpi'] > highest:
   highest = registers['lpi'] 
if 'yo' not in registers.keys(): registers['yo'] = 0 
if 'jh' not in registers.keys(): registers['jh'] = 0 
dec('yo', -634) if registers['jh'] >= -2782 else do_nothing()
if registers['yo'] > highest:
   highest = registers['yo'] 
if 'a' not in registers.keys(): registers['a'] = 0 
if 'jh' not in registers.keys(): registers['jh'] = 0 
inc('a', -111) if registers['jh'] != -2774 else do_nothing()
if registers['a'] > highest:
   highest = registers['a'] 
if 'bfx' not in registers.keys(): registers['bfx'] = 0 
if 'bfx' not in registers.keys(): registers['bfx'] = 0 
inc('bfx', 805) if registers['bfx'] < 3185 else do_nothing()
if registers['bfx'] > highest:
   highest = registers['bfx'] 
if 'ghj' not in registers.keys(): registers['ghj'] = 0 
if 'jh' not in registers.keys(): registers['jh'] = 0 
inc('ghj', -497) if registers['jh'] <= -2771 else do_nothing()
if registers['ghj'] > highest:
   highest = registers['ghj'] 
if 'sh' not in registers.keys(): registers['sh'] = 0 
if 'g' not in registers.keys(): registers['g'] = 0 
inc('sh', 496) if registers['g'] == -543 else do_nothing()
if registers['sh'] > highest:
   highest = registers['sh'] 
if 'ev' not in registers.keys(): registers['ev'] = 0 
if 'jh' not in registers.keys(): registers['jh'] = 0 
dec('ev', 555) if registers['jh'] == -2777 else do_nothing()
if registers['ev'] > highest:
   highest = registers['ev'] 
if 'jq' not in registers.keys(): registers['jq'] = 0 
if 'wfk' not in registers.keys(): registers['wfk'] = 0 
inc('jq', -547) if registers['wfk'] >= -1320 else do_nothing()
if registers['jq'] > highest:
   highest = registers['jq'] 
if 'wfk' not in registers.keys(): registers['wfk'] = 0 
if 'rlq' not in registers.keys(): registers['rlq'] = 0 
inc('wfk', -489) if registers['rlq'] != -256 else do_nothing()
if registers['wfk'] > highest:
   highest = registers['wfk'] 
if 'sh' not in registers.keys(): registers['sh'] = 0 
if 'ev' not in registers.keys(): registers['ev'] = 0 
dec('sh', -212) if registers['ev'] > -2242 else do_nothing()
if registers['sh'] > highest:
   highest = registers['sh'] 
if 'nkr' not in registers.keys(): registers['nkr'] = 0 
if 'vh' not in registers.keys(): registers['vh'] = 0 
dec('nkr', 890) if registers['vh'] == -544 else do_nothing()
if registers['nkr'] > highest:
   highest = registers['nkr'] 
if 't' not in registers.keys(): registers['t'] = 0 
if 'rlq' not in registers.keys(): registers['rlq'] = 0 
inc('t', 639) if registers['rlq'] == -256 else do_nothing()
if registers['t'] > highest:
   highest = registers['t'] 
if 'ghj' not in registers.keys(): registers['ghj'] = 0 
if 'jq' not in registers.keys(): registers['jq'] = 0 
inc('ghj', 397) if registers['jq'] != 3047 else do_nothing()
if registers['ghj'] > highest:
   highest = registers['ghj'] 
if 'qn' not in registers.keys(): registers['qn'] = 0 
if 'bfx' not in registers.keys(): registers['bfx'] = 0 
inc('qn', -489) if registers['bfx'] <= 3992 else do_nothing()
if registers['qn'] > highest:
   highest = registers['qn'] 
if 'rlq' not in registers.keys(): registers['rlq'] = 0 
if 'a' not in registers.keys(): registers['a'] = 0 
dec('rlq', -359) if registers['a'] != -720 else do_nothing()
if registers['rlq'] > highest:
   highest = registers['rlq'] 
if 'u' not in registers.keys(): registers['u'] = 0 
if 't' not in registers.keys(): registers['t'] = 0 
inc('u', -474) if registers['t'] == -1239 else do_nothing()
if registers['u'] > highest:
   highest = registers['u'] 
if 'jh' not in registers.keys(): registers['jh'] = 0 
if 'jh' not in registers.keys(): registers['jh'] = 0 
inc('jh', 205) if registers['jh'] != -2782 else do_nothing()
if registers['jh'] > highest:
   highest = registers['jh'] 
if 't' not in registers.keys(): registers['t'] = 0 
if 'lpi' not in registers.keys(): registers['lpi'] = 0 
inc('t', -581) if registers['lpi'] <= -1514 else do_nothing()
if registers['t'] > highest:
   highest = registers['t'] 
if 'vh' not in registers.keys(): registers['vh'] = 0 
if 'afu' not in registers.keys(): registers['afu'] = 0 
inc('vh', -319) if registers['afu'] <= 1370 else do_nothing()
if registers['vh'] > highest:
   highest = registers['vh'] 
if 'w' not in registers.keys(): registers['w'] = 0 
if 'yo' not in registers.keys(): registers['yo'] = 0 
dec('w', 908) if registers['yo'] > -3248 else do_nothing()
if registers['w'] > highest:
   highest = registers['w'] 
if 'wfk' not in registers.keys(): registers['wfk'] = 0 
if 'qdq' not in registers.keys(): registers['qdq'] = 0 
inc('wfk', 333) if registers['qdq'] < 2528 else do_nothing()
if registers['wfk'] > highest:
   highest = registers['wfk'] 
if 'qn' not in registers.keys(): registers['qn'] = 0 
if 'afu' not in registers.keys(): registers['afu'] = 0 
dec('qn', -736) if registers['afu'] < 1367 else do_nothing()
if registers['qn'] > highest:
   highest = registers['qn'] 
if 'afu' not in registers.keys(): registers['afu'] = 0 
if 't' not in registers.keys(): registers['t'] = 0 
dec('afu', -208) if registers['t'] > -1824 else do_nothing()
if registers['afu'] > highest:
   highest = registers['afu'] 
if 'bfx' not in registers.keys(): registers['bfx'] = 0 
if 'yo' not in registers.keys(): registers['yo'] = 0 
inc('bfx', -918) if registers['yo'] < -3237 else do_nothing()
if registers['bfx'] > highest:
   highest = registers['bfx'] 
if 'a' not in registers.keys(): registers['a'] = 0 
if 'lpi' not in registers.keys(): registers['lpi'] = 0 
dec('a', -729) if registers['lpi'] == -1515 else do_nothing()
if registers['a'] > highest:
   highest = registers['a'] 
if 'u' not in registers.keys(): registers['u'] = 0 
if 'jh' not in registers.keys(): registers['jh'] = 0 
dec('u', -331) if registers['jh'] < -2577 else do_nothing()
if registers['u'] > highest:
   highest = registers['u'] 
if 'pr' not in registers.keys(): registers['pr'] = 0 
if 'ghj' not in registers.keys(): registers['ghj'] = 0 
inc('pr', -364) if registers['ghj'] >= -1480 else do_nothing()
if registers['pr'] > highest:
   highest = registers['pr'] 
if 'fkp' not in registers.keys(): registers['fkp'] = 0 
if 'm' not in registers.keys(): registers['m'] = 0 
dec('fkp', 48) if registers['m'] != 2170 else do_nothing()
if registers['fkp'] > highest:
   highest = registers['fkp'] 
if 'rlq' not in registers.keys(): registers['rlq'] = 0 
if 'jq' not in registers.keys(): registers['jq'] = 0 
inc('rlq', 117) if registers['jq'] <= 3044 else do_nothing()
if registers['rlq'] > highest:
   highest = registers['rlq'] 
if 'qdq' not in registers.keys(): registers['qdq'] = 0 
if 'wfk' not in registers.keys(): registers['wfk'] = 0 
dec('qdq', 867) if registers['wfk'] == -987 else do_nothing()
if registers['qdq'] > highest:
   highest = registers['qdq'] 
if 'fkp' not in registers.keys(): registers['fkp'] = 0 
if 'w' not in registers.keys(): registers['w'] = 0 
inc('fkp', 17) if registers['w'] != 185 else do_nothing()
if registers['fkp'] > highest:
   highest = registers['fkp'] 
if 'lpi' not in registers.keys(): registers['lpi'] = 0 
if 'ghj' not in registers.keys(): registers['ghj'] = 0 
dec('lpi', -5) if registers['ghj'] <= -1472 else do_nothing()
if registers['lpi'] > highest:
   highest = registers['lpi'] 
if 'qrc' not in registers.keys(): registers['qrc'] = 0 
if 'u' not in registers.keys(): registers['u'] = 0 
dec('qrc', -512) if registers['u'] >= -1934 else do_nothing()
if registers['qrc'] > highest:
   highest = registers['qrc'] 
if 'nkr' not in registers.keys(): registers['nkr'] = 0 
if 'g' not in registers.keys(): registers['g'] = 0 
dec('nkr', -110) if registers['g'] < -534 else do_nothing()
if registers['nkr'] > highest:
   highest = registers['nkr'] 
if 'afu' not in registers.keys(): registers['afu'] = 0 
if 'nkr' not in registers.keys(): registers['nkr'] = 0 
dec('afu', -42) if registers['nkr'] != -4076 else do_nothing()
if registers['afu'] > highest:
   highest = registers['afu'] 
if 'w' not in registers.keys(): registers['w'] = 0 
if 'vh' not in registers.keys(): registers['vh'] = 0 
dec('w', 538) if registers['vh'] < -856 else do_nothing()
if registers['w'] > highest:
   highest = registers['w'] 
if 'qrc' not in registers.keys(): registers['qrc'] = 0 
if 'wfk' not in registers.keys(): registers['wfk'] = 0 
inc('qrc', 248) if registers['wfk'] < -978 else do_nothing()
if registers['qrc'] > highest:
   highest = registers['qrc'] 
if 'qrc' not in registers.keys(): registers['qrc'] = 0 
if 'qn' not in registers.keys(): registers['qn'] = 0 
inc('qrc', -797) if registers['qn'] > 3955 else do_nothing()
if registers['qrc'] > highest:
   highest = registers['qrc'] 
if 'yo' not in registers.keys(): registers['yo'] = 0 
if 'jq' not in registers.keys(): registers['jq'] = 0 
dec('yo', -672) if registers['jq'] > 3033 else do_nothing()
if registers['yo'] > highest:
   highest = registers['yo'] 
if 'a' not in registers.keys(): registers['a'] = 0 
if 'qdq' not in registers.keys(): registers['qdq'] = 0 
inc('a', 239) if registers['qdq'] != 1655 else do_nothing()
if registers['a'] > highest:
   highest = registers['a'] 
if 'rlq' not in registers.keys(): registers['rlq'] = 0 
if 'ev' not in registers.keys(): registers['ev'] = 0 
dec('rlq', -568) if registers['ev'] < -2247 else do_nothing()
if registers['rlq'] > highest:
   highest = registers['rlq'] 
if 'g' not in registers.keys(): registers['g'] = 0 
if 'qn' not in registers.keys(): registers['qn'] = 0 
dec('g', 958) if registers['qn'] <= 3952 else do_nothing()
if registers['g'] > highest:
   highest = registers['g'] 
if 'pr' not in registers.keys(): registers['pr'] = 0 
if 'wfk' not in registers.keys(): registers['wfk'] = 0 
inc('pr', 212) if registers['wfk'] > -991 else do_nothing()
if registers['pr'] > highest:
   highest = registers['pr'] 
if 'rlq' not in registers.keys(): registers['rlq'] = 0 
if 'pr' not in registers.keys(): registers['pr'] = 0 
dec('rlq', 674) if registers['pr'] < -5579 else do_nothing()
if registers['rlq'] > highest:
   highest = registers['rlq'] 
if 'm' not in registers.keys(): registers['m'] = 0 
if 'sh' not in registers.keys(): registers['sh'] = 0 
inc('m', 605) if registers['sh'] > 998 else do_nothing()
if registers['m'] > highest:
   highest = registers['m'] 
if 'qn' not in registers.keys(): registers['qn'] = 0 
if 'wfk' not in registers.keys(): registers['wfk'] = 0 
dec('qn', 575) if registers['wfk'] <= -978 else do_nothing()
if registers['qn'] > highest:
   highest = registers['qn'] 
if 'ghj' not in registers.keys(): registers['ghj'] = 0 
if 't' not in registers.keys(): registers['t'] = 0 
inc('ghj', 599) if registers['t'] == -1820 else do_nothing()
if registers['ghj'] > highest:
   highest = registers['ghj'] 
if 'jq' not in registers.keys(): registers['jq'] = 0 
if 'lpi' not in registers.keys(): registers['lpi'] = 0 
dec('jq', -170) if registers['lpi'] == -1510 else do_nothing()
if registers['jq'] > highest:
   highest = registers['jq'] 
if 'ev' not in registers.keys(): registers['ev'] = 0 
if 'qrc' not in registers.keys(): registers['qrc'] = 0 
inc('ev', -832) if registers['qrc'] > -3656 else do_nothing()
if registers['ev'] > highest:
   highest = registers['ev'] 
if 'ev' not in registers.keys(): registers['ev'] = 0 
if 'ghj' not in registers.keys(): registers['ghj'] = 0 
dec('ev', 52) if registers['ghj'] > -869 else do_nothing()
if registers['ev'] > highest:
   highest = registers['ev'] 
if 'vh' not in registers.keys(): registers['vh'] = 0 
if 'u' not in registers.keys(): registers['u'] = 0 
inc('vh', 248) if registers['u'] > -1934 else do_nothing()
if registers['vh'] > highest:
   highest = registers['vh'] 
if 't' not in registers.keys(): registers['t'] = 0 
if 'bfx' not in registers.keys(): registers['bfx'] = 0 
dec('t', 947) if registers['bfx'] != 3075 else do_nothing()
if registers['t'] > highest:
   highest = registers['t'] 
if 'jh' not in registers.keys(): registers['jh'] = 0 
if 'qdq' not in registers.keys(): registers['qdq'] = 0 
inc('jh', 25) if registers['qdq'] > 1654 else do_nothing()
if registers['jh'] > highest:
   highest = registers['jh'] 
if 'sh' not in registers.keys(): registers['sh'] = 0 
if 'qn' not in registers.keys(): registers['qn'] = 0 
inc('sh', 192) if registers['qn'] == 3377 else do_nothing()
if registers['sh'] > highest:
   highest = registers['sh'] 
if 'a' not in registers.keys(): registers['a'] = 0 
if 'yo' not in registers.keys(): registers['yo'] = 0 
inc('a', 861) if registers['yo'] <= -2561 else do_nothing()
if registers['a'] > highest:
   highest = registers['a'] 
if 'yo' not in registers.keys(): registers['yo'] = 0 
if 'm' not in registers.keys(): registers['m'] = 0 
inc('yo', 326) if registers['m'] == 2775 else do_nothing()
if registers['yo'] > highest:
   highest = registers['yo'] 
if 'afu' not in registers.keys(): registers['afu'] = 0 
if 'g' not in registers.keys(): registers['g'] = 0 
dec('afu', -180) if registers['g'] >= -1502 else do_nothing()
if registers['afu'] > highest:
   highest = registers['afu'] 
if 'fkp' not in registers.keys(): registers['fkp'] = 0 
if 'bfx' not in registers.keys(): registers['bfx'] = 0 
dec('fkp', -489) if registers['bfx'] == 3067 else do_nothing()
if registers['fkp'] > highest:
   highest = registers['fkp'] 
if 'jh' not in registers.keys(): registers['jh'] = 0 
if 'afu' not in registers.keys(): registers['afu'] = 0 
dec('jh', 902) if registers['afu'] > 1787 else do_nothing()
if registers['jh'] > highest:
   highest = registers['jh'] 
if 'u' not in registers.keys(): registers['u'] = 0 
if 'ghj' not in registers.keys(): registers['ghj'] = 0 
inc('u', -116) if registers['ghj'] != -866 else do_nothing()
if registers['u'] > highest:
   highest = registers['u'] 
if 'afu' not in registers.keys(): registers['afu'] = 0 
if 'g' not in registers.keys(): registers['g'] = 0 
dec('afu', 854) if registers['g'] >= -1505 else do_nothing()
if registers['afu'] > highest:
   highest = registers['afu'] 
if 'pr' not in registers.keys(): registers['pr'] = 0 
if 'pr' not in registers.keys(): registers['pr'] = 0 
dec('pr', 207) if registers['pr'] != -5578 else do_nothing()
if registers['pr'] > highest:
   highest = registers['pr'] 
if 'jq' not in registers.keys(): registers['jq'] = 0 
if 'rlq' not in registers.keys(): registers['rlq'] = 0 
dec('jq', 600) if registers['rlq'] >= -458 else do_nothing()
if registers['jq'] > highest:
   highest = registers['jq'] 
if 'fkp' not in registers.keys(): registers['fkp'] = 0 
if 'afu' not in registers.keys(): registers['afu'] = 0 
dec('fkp', -550) if registers['afu'] <= 946 else do_nothing()
if registers['fkp'] > highest:
   highest = registers['fkp'] 
if 'qn' not in registers.keys(): registers['qn'] = 0 
if 'g' not in registers.keys(): registers['g'] = 0 
inc('qn', 374) if registers['g'] >= -1509 else do_nothing()
if registers['qn'] > highest:
   highest = registers['qn'] 
if 'afu' not in registers.keys(): registers['afu'] = 0 
if 'pr' not in registers.keys(): registers['pr'] = 0 
inc('afu', -143) if registers['pr'] != -5793 else do_nothing()
if registers['afu'] > highest:
   highest = registers['afu'] 
if 'qdq' not in registers.keys(): registers['qdq'] = 0 
if 'rlq' not in registers.keys(): registers['rlq'] = 0 
dec('qdq', 649) if registers['rlq'] != -460 else do_nothing()
if registers['qdq'] > highest:
   highest = registers['qdq'] 
if 'wfk' not in registers.keys(): registers['wfk'] = 0 
if 'lpi' not in registers.keys(): registers['lpi'] = 0 
dec('wfk', 250) if registers['lpi'] < -1508 else do_nothing()
if registers['wfk'] > highest:
   highest = registers['wfk'] 
if 't' not in registers.keys(): registers['t'] = 0 
if 'vh' not in registers.keys(): registers['vh'] = 0 
dec('t', 61) if registers['vh'] >= -620 else do_nothing()
if registers['t'] > highest:
   highest = registers['t'] 
if 'afu' not in registers.keys(): registers['afu'] = 0 
if 'vh' not in registers.keys(): registers['vh'] = 0 
inc('afu', -194) if registers['vh'] == -612 else do_nothing()
if registers['afu'] > highest:
   highest = registers['afu'] 
if 'jh' not in registers.keys(): registers['jh'] = 0 
if 'k' not in registers.keys(): registers['k'] = 0 
inc('jh', -33) if registers['k'] > 3423 else do_nothing()
if registers['jh'] > highest:
   highest = registers['jh'] 
if 'jh' not in registers.keys(): registers['jh'] = 0 
if 'bfx' not in registers.keys(): registers['bfx'] = 0 
dec('jh', -233) if registers['bfx'] != 3073 else do_nothing()
if registers['jh'] > highest:
   highest = registers['jh'] 
if 'qrc' not in registers.keys(): registers['qrc'] = 0 
if 'jh' not in registers.keys(): registers['jh'] = 0 
inc('qrc', -159) if registers['jh'] < -3244 else do_nothing()
if registers['qrc'] > highest:
   highest = registers['qrc'] 
if 'jq' not in registers.keys(): registers['jq'] = 0 
if 'fkp' not in registers.keys(): registers['fkp'] = 0 
inc('jq', 608) if registers['fkp'] <= 3491 else do_nothing()
if registers['jq'] > highest:
   highest = registers['jq'] 
if 'bfx' not in registers.keys(): registers['bfx'] = 0 
if 'pr' not in registers.keys(): registers['pr'] = 0 
dec('bfx', -19) if registers['pr'] == -5790 else do_nothing()
if registers['bfx'] > highest:
   highest = registers['bfx'] 
if 't' not in registers.keys(): registers['t'] = 0 
if 'ev' not in registers.keys(): registers['ev'] = 0 
dec('t', -942) if registers['ev'] != -3080 else do_nothing()
if registers['t'] > highest:
   highest = registers['t'] 
if 'g' not in registers.keys(): registers['g'] = 0 
if 'wfk' not in registers.keys(): registers['wfk'] = 0 
dec('g', -356) if registers['wfk'] == -1247 else do_nothing()
if registers['g'] > highest:
   highest = registers['g'] 
if 'yo' not in registers.keys(): registers['yo'] = 0 
if 'qdq' not in registers.keys(): registers['qdq'] = 0 
dec('yo', 172) if registers['qdq'] <= 1007 else do_nothing()
if registers['yo'] > highest:
   highest = registers['yo'] 
if 'fkp' not in registers.keys(): registers['fkp'] = 0 
if 'lpi' not in registers.keys(): registers['lpi'] = 0 
inc('fkp', 791) if registers['lpi'] > -1511 else do_nothing()
if registers['fkp'] > highest:
   highest = registers['fkp'] 
if 'jh' not in registers.keys(): registers['jh'] = 0 
if 'lpi' not in registers.keys(): registers['lpi'] = 0 
inc('jh', 244) if registers['lpi'] > -1513 else do_nothing()
if registers['jh'] > highest:
   highest = registers['jh'] 
if 'afu' not in registers.keys(): registers['afu'] = 0 
if 'qn' not in registers.keys(): registers['qn'] = 0 
dec('afu', 891) if registers['qn'] == 3751 else do_nothing()
if registers['afu'] > highest:
   highest = registers['afu'] 
if 'yo' not in registers.keys(): registers['yo'] = 0 
if 'jh' not in registers.keys(): registers['jh'] = 0 
dec('yo', -23) if registers['jh'] == -3005 else do_nothing()
if registers['yo'] > highest:
   highest = registers['yo'] 
if 'ghj' not in registers.keys(): registers['ghj'] = 0 
if 'ghj' not in registers.keys(): registers['ghj'] = 0 
dec('ghj', 451) if registers['ghj'] == -873 else do_nothing()
if registers['ghj'] > highest:
   highest = registers['ghj'] 
if 'jh' not in registers.keys(): registers['jh'] = 0 
if 'g' not in registers.keys(): registers['g'] = 0 
dec('jh', 202) if registers['g'] < -1497 else do_nothing()
if registers['jh'] > highest:
   highest = registers['jh'] 
if 'qdq' not in registers.keys(): registers['qdq'] = 0 
if 't' not in registers.keys(): registers['t'] = 0 
inc('qdq', 876) if registers['t'] < -1895 else do_nothing()
if registers['qdq'] > highest:
   highest = registers['qdq'] 
if 'sh' not in registers.keys(): registers['sh'] = 0 
if 'k' not in registers.keys(): registers['k'] = 0 
inc('sh', 698) if registers['k'] < 3438 else do_nothing()
if registers['sh'] > highest:
   highest = registers['sh'] 
if 'sh' not in registers.keys(): registers['sh'] = 0 
if 'afu' not in registers.keys(): registers['afu'] = 0 
dec('sh', 836) if registers['afu'] != -82 else do_nothing()
if registers['sh'] > highest:
   highest = registers['sh'] 
if 'lpi' not in registers.keys(): registers['lpi'] = 0 
if 'a' not in registers.keys(): registers['a'] = 0 
dec('lpi', -928) if registers['a'] > 875 else do_nothing()
if registers['lpi'] > highest:
   highest = registers['lpi'] 
if 'jh' not in registers.keys(): registers['jh'] = 0 
if 'qdq' not in registers.keys(): registers['qdq'] = 0 
inc('jh', 730) if registers['qdq'] < 1011 else do_nothing()
if registers['jh'] > highest:
   highest = registers['jh'] 
if 'bfx' not in registers.keys(): registers['bfx'] = 0 
if 'qn' not in registers.keys(): registers['qn'] = 0 
inc('bfx', -318) if registers['qn'] <= 3752 else do_nothing()
if registers['bfx'] > highest:
   highest = registers['bfx'] 
if 'k' not in registers.keys(): registers['k'] = 0 
if 'rlq' not in registers.keys(): registers['rlq'] = 0 
dec('k', -329) if registers['rlq'] >= -448 else do_nothing()
if registers['k'] > highest:
   highest = registers['k'] 
if 'lpi' not in registers.keys(): registers['lpi'] = 0 
if 'pr' not in registers.keys(): registers['pr'] = 0 
inc('lpi', 354) if registers['pr'] > -5793 else do_nothing()
if registers['lpi'] > highest:
   highest = registers['lpi'] 
if 'lpi' not in registers.keys(): registers['lpi'] = 0 
if 'fkp' not in registers.keys(): registers['fkp'] = 0 
inc('lpi', -937) if registers['fkp'] == 4287 else do_nothing()
if registers['lpi'] > highest:
   highest = registers['lpi'] 
if 'wfk' not in registers.keys(): registers['wfk'] = 0 
if 'nkr' not in registers.keys(): registers['nkr'] = 0 
inc('wfk', -267) if registers['nkr'] >= -4073 else do_nothing()
if registers['wfk'] > highest:
   highest = registers['wfk'] 
if 'bfx' not in registers.keys(): registers['bfx'] = 0 
if 't' not in registers.keys(): registers['t'] = 0 
inc('bfx', 466) if registers['t'] != -1881 else do_nothing()
if registers['bfx'] > highest:
   highest = registers['bfx'] 
if 't' not in registers.keys(): registers['t'] = 0 
if 'rlq' not in registers.keys(): registers['rlq'] = 0 
inc('t', -841) if registers['rlq'] != -461 else do_nothing()
if registers['t'] > highest:
   highest = registers['t'] 
if 'w' not in registers.keys(): registers['w'] = 0 
if 'm' not in registers.keys(): registers['m'] = 0 
inc('w', 135) if registers['m'] < 2781 else do_nothing()
if registers['w'] > highest:
   highest = registers['w'] 
if 'u' not in registers.keys(): registers['u'] = 0 
if 'qdq' not in registers.keys(): registers['qdq'] = 0 
inc('u', -861) if registers['qdq'] <= 1012 else do_nothing()
if registers['u'] > highest:
   highest = registers['u'] 
if 'wfk' not in registers.keys(): registers['wfk'] = 0 
if 'jh' not in registers.keys(): registers['jh'] = 0 
dec('wfk', -66) if registers['jh'] < -2469 else do_nothing()
if registers['wfk'] > highest:
   highest = registers['wfk'] 
if 'w' not in registers.keys(): registers['w'] = 0 
if 'ghj' not in registers.keys(): registers['ghj'] = 0 
dec('w', -527) if registers['ghj'] != -1324 else do_nothing()
if registers['w'] > highest:
   highest = registers['w'] 
if 'g' not in registers.keys(): registers['g'] = 0 
if 'k' not in registers.keys(): registers['k'] = 0 
dec('g', -560) if registers['k'] < 3435 else do_nothing()
if registers['g'] > highest:
   highest = registers['g'] 
if 'lpi' not in registers.keys(): registers['lpi'] = 0 
if 'qrc' not in registers.keys(): registers['qrc'] = 0 
inc('lpi', 907) if registers['qrc'] != -3810 else do_nothing()
if registers['lpi'] > highest:
   highest = registers['lpi'] 
if 'qdq' not in registers.keys(): registers['qdq'] = 0 
if 'pr' not in registers.keys(): registers['pr'] = 0 
dec('qdq', -423) if registers['pr'] >= -5795 else do_nothing()
if registers['qdq'] > highest:
   highest = registers['qdq'] 
if 'bfx' not in registers.keys(): registers['bfx'] = 0 
if 'qdq' not in registers.keys(): registers['qdq'] = 0 
inc('bfx', -118) if registers['qdq'] == 1429 else do_nothing()
if registers['bfx'] > highest:
   highest = registers['bfx'] 
if 'pr' not in registers.keys(): registers['pr'] = 0 
if 'qrc' not in registers.keys(): registers['qrc'] = 0 
inc('pr', -918) if registers['qrc'] <= -3806 else do_nothing()
if registers['pr'] > highest:
   highest = registers['pr'] 
if 'a' not in registers.keys(): registers['a'] = 0 
if 'ghj' not in registers.keys(): registers['ghj'] = 0 
dec('a', -127) if registers['ghj'] <= -1317 else do_nothing()
if registers['a'] > highest:
   highest = registers['a'] 
if 'qn' not in registers.keys(): registers['qn'] = 0 
if 'm' not in registers.keys(): registers['m'] = 0 
dec('qn', -740) if registers['m'] > 2768 else do_nothing()
if registers['qn'] > highest:
   highest = registers['qn'] 
if 'qdq' not in registers.keys(): registers['qdq'] = 0 
if 'yo' not in registers.keys(): registers['yo'] = 0 
inc('qdq', -431) if registers['yo'] <= -2391 else do_nothing()
if registers['qdq'] > highest:
   highest = registers['qdq'] 
if 'nkr' not in registers.keys(): registers['nkr'] = 0 
if 'rlq' not in registers.keys(): registers['rlq'] = 0 
inc('nkr', 80) if registers['rlq'] < -456 else do_nothing()
if registers['nkr'] > highest:
   highest = registers['nkr'] 
if 'jh' not in registers.keys(): registers['jh'] = 0 
if 'w' not in registers.keys(): registers['w'] = 0 
dec('jh', -189) if registers['w'] <= -235 else do_nothing()
if registers['jh'] > highest:
   highest = registers['jh'] 
if 'w' not in registers.keys(): registers['w'] = 0 
if 'afu' not in registers.keys(): registers['afu'] = 0 
inc('w', 651) if registers['afu'] >= -93 else do_nothing()
if registers['w'] > highest:
   highest = registers['w'] 
if 'jq' not in registers.keys(): registers['jq'] = 0 
if 'w' not in registers.keys(): registers['w'] = 0 
dec('jq', -455) if registers['w'] > 417 else do_nothing()
if registers['jq'] > highest:
   highest = registers['jq'] 
if 'qdq' not in registers.keys(): registers['qdq'] = 0 
if 't' not in registers.keys(): registers['t'] = 0 
dec('qdq', 756) if registers['t'] <= -2725 else do_nothing()
if registers['qdq'] > highest:
   highest = registers['qdq'] 
if 'qdq' not in registers.keys(): registers['qdq'] = 0 
if 'ev' not in registers.keys(): registers['ev'] = 0 
inc('qdq', -869) if registers['ev'] != -3071 else do_nothing()
if registers['qdq'] > highest:
   highest = registers['qdq'] 
if 'ev' not in registers.keys(): registers['ev'] = 0 
if 'qdq' not in registers.keys(): registers['qdq'] = 0 
dec('ev', -161) if registers['qdq'] != -624 else do_nothing()
if registers['ev'] > highest:
   highest = registers['ev'] 
if 'a' not in registers.keys(): registers['a'] = 0 
if 'qn' not in registers.keys(): registers['qn'] = 0 
dec('a', -717) if registers['qn'] < 4495 else do_nothing()
if registers['a'] > highest:
   highest = registers['a'] 
if 'pr' not in registers.keys(): registers['pr'] = 0 
if 't' not in registers.keys(): registers['t'] = 0 
inc('pr', -134) if registers['t'] > -2731 else do_nothing()
if registers['pr'] > highest:
   highest = registers['pr'] 
if 'ev' not in registers.keys(): registers['ev'] = 0 
if 'jh' not in registers.keys(): registers['jh'] = 0 
inc('ev', -592) if registers['jh'] != -2485 else do_nothing()
if registers['ev'] > highest:
   highest = registers['ev'] 
if 'a' not in registers.keys(): registers['a'] = 0 
if 'u' not in registers.keys(): registers['u'] = 0 
dec('a', 850) if registers['u'] >= -2912 else do_nothing()
if registers['a'] > highest:
   highest = registers['a'] 
if 'jq' not in registers.keys(): registers['jq'] = 0 
if 'ghj' not in registers.keys(): registers['ghj'] = 0 
inc('jq', -399) if registers['ghj'] == -1324 else do_nothing()
if registers['jq'] > highest:
   highest = registers['jq'] 
if 'nkr' not in registers.keys(): registers['nkr'] = 0 
if 't' not in registers.keys(): registers['t'] = 0 
dec('nkr', 423) if registers['t'] >= -2734 else do_nothing()
if registers['nkr'] > highest:
   highest = registers['nkr'] 
if 'vh' not in registers.keys(): registers['vh'] = 0 
if 'wfk' not in registers.keys(): registers['wfk'] = 0 
dec('vh', 860) if registers['wfk'] != -1439 else do_nothing()
if registers['vh'] > highest:
   highest = registers['vh'] 
if 'sh' not in registers.keys(): registers['sh'] = 0 
if 'g' not in registers.keys(): registers['g'] = 0 
inc('sh', 475) if registers['g'] >= -946 else do_nothing()
if registers['sh'] > highest:
   highest = registers['sh'] 
if 't' not in registers.keys(): registers['t'] = 0 
if 'k' not in registers.keys(): registers['k'] = 0 
inc('t', 33) if registers['k'] >= 3436 else do_nothing()
if registers['t'] > highest:
   highest = registers['t'] 
if 'qdq' not in registers.keys(): registers['qdq'] = 0 
if 'bfx' not in registers.keys(): registers['bfx'] = 0 
inc('qdq', 183) if registers['bfx'] != 3124 else do_nothing()
if registers['qdq'] > highest:
   highest = registers['qdq'] 
if 'm' not in registers.keys(): registers['m'] = 0 
if 'pr' not in registers.keys(): registers['pr'] = 0 
dec('m', 802) if registers['pr'] < -6841 else do_nothing()
if registers['m'] > highest:
   highest = registers['m'] 
if 'a' not in registers.keys(): registers['a'] = 0 
if 'fkp' not in registers.keys(): registers['fkp'] = 0 
inc('a', 579) if registers['fkp'] != 4282 else do_nothing()
if registers['a'] > highest:
   highest = registers['a'] 
if 'qdq' not in registers.keys(): registers['qdq'] = 0 
if 'ghj' not in registers.keys(): registers['ghj'] = 0 
dec('qdq', 705) if registers['ghj'] != -1324 else do_nothing()
if registers['qdq'] > highest:
   highest = registers['qdq'] 
if 'qn' not in registers.keys(): registers['qn'] = 0 
if 'afu' not in registers.keys(): registers['afu'] = 0 
inc('qn', 856) if registers['afu'] > -101 else do_nothing()
if registers['qn'] > highest:
   highest = registers['qn'] 
if 'vh' not in registers.keys(): registers['vh'] = 0 
if 'qn' not in registers.keys(): registers['qn'] = 0 
inc('vh', -856) if registers['qn'] < 5354 else do_nothing()
if registers['vh'] > highest:
   highest = registers['vh'] 
if 't' not in registers.keys(): registers['t'] = 0 
if 'bfx' not in registers.keys(): registers['bfx'] = 0 
dec('t', 80) if registers['bfx'] != 3115 else do_nothing()
if registers['t'] > highest:
   highest = registers['t'] 
if 'qn' not in registers.keys(): registers['qn'] = 0 
if 'a' not in registers.keys(): registers['a'] = 0 
inc('qn', -881) if registers['a'] < 1456 else do_nothing()
if registers['qn'] > highest:
   highest = registers['qn'] 
if 'pr' not in registers.keys(): registers['pr'] = 0 
if 'wfk' not in registers.keys(): registers['wfk'] = 0 
inc('pr', -772) if registers['wfk'] <= -1436 else do_nothing()
if registers['pr'] > highest:
   highest = registers['pr'] 
if 't' not in registers.keys(): registers['t'] = 0 
if 'rlq' not in registers.keys(): registers['rlq'] = 0 
inc('t', -874) if registers['rlq'] == -446 else do_nothing()
if registers['t'] > highest:
   highest = registers['t'] 
if 'wfk' not in registers.keys(): registers['wfk'] = 0 
if 'rlq' not in registers.keys(): registers['rlq'] = 0 
inc('wfk', -710) if registers['rlq'] < -451 else do_nothing()
if registers['wfk'] > highest:
   highest = registers['wfk'] 
if 'wfk' not in registers.keys(): registers['wfk'] = 0 
if 'vh' not in registers.keys(): registers['vh'] = 0 
dec('wfk', -584) if registers['vh'] > -2339 else do_nothing()
if registers['wfk'] > highest:
   highest = registers['wfk'] 
if 'pr' not in registers.keys(): registers['pr'] = 0 
if 'pr' not in registers.keys(): registers['pr'] = 0 
dec('pr', 41) if registers['pr'] == -7614 else do_nothing()
if registers['pr'] > highest:
   highest = registers['pr'] 
if 'vh' not in registers.keys(): registers['vh'] = 0 
if 'jh' not in registers.keys(): registers['jh'] = 0 
dec('vh', 430) if registers['jh'] > -2487 else do_nothing()
if registers['vh'] > highest:
   highest = registers['vh'] 
if 'qn' not in registers.keys(): registers['qn'] = 0 
if 'sh' not in registers.keys(): registers['sh'] = 0 
dec('qn', 736) if registers['sh'] < 1542 else do_nothing()
if registers['qn'] > highest:
   highest = registers['qn'] 
if 'w' not in registers.keys(): registers['w'] = 0 
if 'u' not in registers.keys(): registers['u'] = 0 
inc('w', 912) if registers['u'] <= -2909 else do_nothing()
if registers['w'] > highest:
   highest = registers['w'] 
if 'lpi' not in registers.keys(): registers['lpi'] = 0 
if 'lpi' not in registers.keys(): registers['lpi'] = 0 
inc('lpi', -469) if registers['lpi'] >= -2095 else do_nothing()
if registers['lpi'] > highest:
   highest = registers['lpi'] 
if 'u' not in registers.keys(): registers['u'] = 0 
if 'vh' not in registers.keys(): registers['vh'] = 0 
inc('u', 981) if registers['vh'] > -2760 else do_nothing()
if registers['u'] > highest:
   highest = registers['u'] 
if 'sh' not in registers.keys(): registers['sh'] = 0 
if 'lpi' not in registers.keys(): registers['lpi'] = 0 
inc('sh', -884) if registers['lpi'] > -2565 else do_nothing()
if registers['sh'] > highest:
   highest = registers['sh'] 
if 'qrc' not in registers.keys(): registers['qrc'] = 0 
if 'sh' not in registers.keys(): registers['sh'] = 0 
dec('qrc', -832) if registers['sh'] >= 642 else do_nothing()
if registers['qrc'] > highest:
   highest = registers['qrc'] 
if 'lpi' not in registers.keys(): registers['lpi'] = 0 
if 'jh' not in registers.keys(): registers['jh'] = 0 
dec('lpi', -139) if registers['jh'] != -2480 else do_nothing()
if registers['lpi'] > highest:
   highest = registers['lpi'] 
if 'w' not in registers.keys(): registers['w'] = 0 
if 'w' not in registers.keys(): registers['w'] = 0 
inc('w', -369) if registers['w'] > 1339 else do_nothing()
if registers['w'] > highest:
   highest = registers['w'] 
if 'qrc' not in registers.keys(): registers['qrc'] = 0 
if 'lpi' not in registers.keys(): registers['lpi'] = 0 
dec('qrc', -470) if registers['lpi'] < -2419 else do_nothing()
if registers['qrc'] > highest:
   highest = registers['qrc'] 
if 'qdq' not in registers.keys(): registers['qdq'] = 0 
if 'qrc' not in registers.keys(): registers['qrc'] = 0 
dec('qdq', 535) if registers['qrc'] < -2501 else do_nothing()
if registers['qdq'] > highest:
   highest = registers['qdq'] 
if 'm' not in registers.keys(): registers['m'] = 0 
if 'rlq' not in registers.keys(): registers['rlq'] = 0 
dec('m', -160) if registers['rlq'] < -449 else do_nothing()
if registers['m'] > highest:
   highest = registers['m'] 
if 'm' not in registers.keys(): registers['m'] = 0 
if 'qrc' not in registers.keys(): registers['qrc'] = 0 
inc('m', 480) if registers['qrc'] != -2501 else do_nothing()
if registers['m'] > highest:
   highest = registers['m'] 
if 'jq' not in registers.keys(): registers['jq'] = 0 
if 'ghj' not in registers.keys(): registers['ghj'] = 0 
dec('jq', 46) if registers['ghj'] >= -1324 else do_nothing()
if registers['jq'] > highest:
   highest = registers['jq'] 
if 'fkp' not in registers.keys(): registers['fkp'] = 0 
if 'nkr' not in registers.keys(): registers['nkr'] = 0 
inc('fkp', 691) if registers['nkr'] == -4501 else do_nothing()
if registers['fkp'] > highest:
   highest = registers['fkp'] 
if 'm' not in registers.keys(): registers['m'] = 0 
if 'pr' not in registers.keys(): registers['pr'] = 0 
inc('m', -364) if registers['pr'] != -7658 else do_nothing()
if registers['m'] > highest:
   highest = registers['m'] 
if 'ghj' not in registers.keys(): registers['ghj'] = 0 
if 'nkr' not in registers.keys(): registers['nkr'] = 0 
inc('ghj', 619) if registers['nkr'] < -4502 else do_nothing()
if registers['ghj'] > highest:
   highest = registers['ghj'] 
if 'wfk' not in registers.keys(): registers['wfk'] = 0 
if 'qdq' not in registers.keys(): registers['qdq'] = 0 
inc('wfk', 99) if registers['qdq'] == -979 else do_nothing()
if registers['wfk'] > highest:
   highest = registers['wfk'] 
if 't' not in registers.keys(): registers['t'] = 0 
if 'nkr' not in registers.keys(): registers['nkr'] = 0 
inc('t', -494) if registers['nkr'] < -4486 else do_nothing()
if registers['t'] > highest:
   highest = registers['t'] 
if 'jh' not in registers.keys(): registers['jh'] = 0 
if 'jh' not in registers.keys(): registers['jh'] = 0 
inc('jh', 243) if registers['jh'] == -2477 else do_nothing()
if registers['jh'] > highest:
   highest = registers['jh'] 
if 'bfx' not in registers.keys(): registers['bfx'] = 0 
if 'pr' not in registers.keys(): registers['pr'] = 0 
inc('bfx', 446) if registers['pr'] >= -7658 else do_nothing()
if registers['bfx'] > highest:
   highest = registers['bfx'] 
if 'sh' not in registers.keys(): registers['sh'] = 0 
if 'ghj' not in registers.keys(): registers['ghj'] = 0 
dec('sh', -137) if registers['ghj'] <= -1321 else do_nothing()
if registers['sh'] > highest:
   highest = registers['sh'] 
if 'pr' not in registers.keys(): registers['pr'] = 0 
if 'jq' not in registers.keys(): registers['jq'] = 0 
inc('pr', 782) if registers['jq'] >= 2615 else do_nothing()
if registers['pr'] > highest:
   highest = registers['pr'] 
if 'pr' not in registers.keys(): registers['pr'] = 0 
if 'u' not in registers.keys(): registers['u'] = 0 
inc('pr', 341) if registers['u'] < -2918 else do_nothing()
if registers['pr'] > highest:
   highest = registers['pr'] 
if 'jh' not in registers.keys(): registers['jh'] = 0 
if 'jq' not in registers.keys(): registers['jq'] = 0 
dec('jh', -195) if registers['jq'] == 2622 else do_nothing()
if registers['jh'] > highest:
   highest = registers['jh'] 
if 'jh' not in registers.keys(): registers['jh'] = 0 
if 'qn' not in registers.keys(): registers['qn'] = 0 
inc('jh', -738) if registers['qn'] >= 3726 else do_nothing()
if registers['jh'] > highest:
   highest = registers['jh'] 
if 'k' not in registers.keys(): registers['k'] = 0 
if 'pr' not in registers.keys(): registers['pr'] = 0 
inc('k', -678) if registers['pr'] <= -6864 else do_nothing()
if registers['k'] > highest:
   highest = registers['k'] 
if 'bfx' not in registers.keys(): registers['bfx'] = 0 
if 'vh' not in registers.keys(): registers['vh'] = 0 
dec('bfx', 895) if registers['vh'] < -2760 else do_nothing()
if registers['bfx'] > highest:
   highest = registers['bfx'] 
if 'nkr' not in registers.keys(): registers['nkr'] = 0 
if 'qdq' not in registers.keys(): registers['qdq'] = 0 
inc('nkr', -511) if registers['qdq'] < -980 else do_nothing()
if registers['nkr'] > highest:
   highest = registers['nkr'] 
if 'afu' not in registers.keys(): registers['afu'] = 0 
if 'm' not in registers.keys(): registers['m'] = 0 
dec('afu', 443) if registers['m'] == 2249 else do_nothing()
if registers['afu'] > highest:
   highest = registers['afu'] 
if 'k' not in registers.keys(): registers['k'] = 0 
if 'bfx' not in registers.keys(): registers['bfx'] = 0 
inc('k', -192) if registers['bfx'] == 2667 else do_nothing()
if registers['k'] > highest:
   highest = registers['k'] 
if 'qdq' not in registers.keys(): registers['qdq'] = 0 
if 'qdq' not in registers.keys(): registers['qdq'] = 0 
dec('qdq', 773) if registers['qdq'] != -980 else do_nothing()
if registers['qdq'] > highest:
   highest = registers['qdq'] 
if 'u' not in registers.keys(): registers['u'] = 0 
if 'ghj' not in registers.keys(): registers['ghj'] = 0 
dec('u', -371) if registers['ghj'] <= -1319 else do_nothing()
if registers['u'] > highest:
   highest = registers['u'] 
if 't' not in registers.keys(): registers['t'] = 0 
if 'a' not in registers.keys(): registers['a'] = 0 
dec('t', 235) if registers['a'] >= 1442 else do_nothing()
if registers['t'] > highest:
   highest = registers['t'] 
if 'lpi' not in registers.keys(): registers['lpi'] = 0 
if 'jh' not in registers.keys(): registers['jh'] = 0 
dec('lpi', 575) if registers['jh'] >= -2774 else do_nothing()
if registers['lpi'] > highest:
   highest = registers['lpi'] 
if 'k' not in registers.keys(): registers['k'] = 0 
if 'yo' not in registers.keys(): registers['yo'] = 0 
dec('k', -185) if registers['yo'] < -2389 else do_nothing()
if registers['k'] > highest:
   highest = registers['k'] 
if 'rlq' not in registers.keys(): registers['rlq'] = 0 
if 'lpi' not in registers.keys(): registers['lpi'] = 0 
dec('rlq', 663) if registers['lpi'] <= -2421 else do_nothing()
if registers['rlq'] > highest:
   highest = registers['rlq'] 
if 'a' not in registers.keys(): registers['a'] = 0 
if 'vh' not in registers.keys(): registers['vh'] = 0 
dec('a', 56) if registers['vh'] < -2758 else do_nothing()
if registers['a'] > highest:
   highest = registers['a'] 
if 'ghj' not in registers.keys(): registers['ghj'] = 0 
if 'ev' not in registers.keys(): registers['ev'] = 0 
inc('ghj', -81) if registers['ev'] > -3504 else do_nothing()
if registers['ghj'] > highest:
   highest = registers['ghj'] 
if 'pr' not in registers.keys(): registers['pr'] = 0 
if 'ev' not in registers.keys(): registers['ev'] = 0 
inc('pr', 276) if registers['ev'] > -3505 else do_nothing()
if registers['pr'] > highest:
   highest = registers['pr'] 
if 'u' not in registers.keys(): registers['u'] = 0 
if 't' not in registers.keys(): registers['t'] = 0 
dec('u', -402) if registers['t'] >= -3535 else do_nothing()
if registers['u'] > highest:
   highest = registers['u'] 
if 'vh' not in registers.keys(): registers['vh'] = 0 
if 'w' not in registers.keys(): registers['w'] = 0 
inc('vh', 968) if registers['w'] > 1333 else do_nothing()
if registers['vh'] > highest:
   highest = registers['vh'] 
if 'ghj' not in registers.keys(): registers['ghj'] = 0 
if 'rlq' not in registers.keys(): registers['rlq'] = 0 
dec('ghj', -413) if registers['rlq'] != -1124 else do_nothing()
if registers['ghj'] > highest:
   highest = registers['ghj'] 
if 'ev' not in registers.keys(): registers['ev'] = 0 
if 'qn' not in registers.keys(): registers['qn'] = 0 
inc('ev', 846) if registers['qn'] < 3733 else do_nothing()
if registers['ev'] > highest:
   highest = registers['ev'] 
if 'nkr' not in registers.keys(): registers['nkr'] = 0 
if 'k' not in registers.keys(): registers['k'] = 0 
inc('nkr', -604) if registers['k'] > 2743 else do_nothing()
if registers['nkr'] > highest:
   highest = registers['nkr'] 
if 't' not in registers.keys(): registers['t'] = 0 
if 'sh' not in registers.keys(): registers['sh'] = 0 
inc('t', -165) if registers['sh'] <= 775 else do_nothing()
if registers['t'] > highest:
   highest = registers['t'] 
if 'ev' not in registers.keys(): registers['ev'] = 0 
if 'a' not in registers.keys(): registers['a'] = 0 
dec('ev', 16) if registers['a'] > 1388 else do_nothing()
if registers['ev'] > highest:
   highest = registers['ev'] 
if 'm' not in registers.keys(): registers['m'] = 0 
if 'afu' not in registers.keys(): registers['afu'] = 0 
inc('m', -148) if registers['afu'] != -532 else do_nothing()
if registers['m'] > highest:
   highest = registers['m'] 
if 'nkr' not in registers.keys(): registers['nkr'] = 0 
if 'u' not in registers.keys(): registers['u'] = 0 
inc('nkr', -877) if registers['u'] < -2533 else do_nothing()
if registers['nkr'] > highest:
   highest = registers['nkr'] 
if 'k' not in registers.keys(): registers['k'] = 0 
if 'wfk' not in registers.keys(): registers['wfk'] = 0 
inc('k', -785) if registers['wfk'] > -1474 else do_nothing()
if registers['k'] > highest:
   highest = registers['k'] 
if 'jq' not in registers.keys(): registers['jq'] = 0 
if 'fkp' not in registers.keys(): registers['fkp'] = 0 
inc('jq', 896) if registers['fkp'] > 4281 else do_nothing()
if registers['jq'] > highest:
   highest = registers['jq'] 
if 'ghj' not in registers.keys(): registers['ghj'] = 0 
if 'ghj' not in registers.keys(): registers['ghj'] = 0 
dec('ghj', -659) if registers['ghj'] != -911 else do_nothing()
if registers['ghj'] > highest:
   highest = registers['ghj'] 
if 'k' not in registers.keys(): registers['k'] = 0 
if 'afu' not in registers.keys(): registers['afu'] = 0 
dec('k', 432) if registers['afu'] >= -534 else do_nothing()
if registers['k'] > highest:
   highest = registers['k'] 
if 'nkr' not in registers.keys(): registers['nkr'] = 0 
if 'qdq' not in registers.keys(): registers['qdq'] = 0 
dec('nkr', 57) if registers['qdq'] <= -1743 else do_nothing()
if registers['nkr'] > highest:
   highest = registers['nkr'] 
if 'qn' not in registers.keys(): registers['qn'] = 0 
if 'm' not in registers.keys(): registers['m'] = 0 
inc('qn', -324) if registers['m'] != 2101 else do_nothing()
if registers['qn'] > highest:
   highest = registers['qn'] 
if 'qn' not in registers.keys(): registers['qn'] = 0 
if 'm' not in registers.keys(): registers['m'] = 0 
inc('qn', 522) if registers['m'] <= 2107 else do_nothing()
if registers['qn'] > highest:
   highest = registers['qn'] 
if 'sh' not in registers.keys(): registers['sh'] = 0 
if 'k' not in registers.keys(): registers['k'] = 0 
inc('sh', 201) if registers['k'] == 1520 else do_nothing()
if registers['sh'] > highest:
   highest = registers['sh'] 
if 'rlq' not in registers.keys(): registers['rlq'] = 0 
if 'pr' not in registers.keys(): registers['pr'] = 0 
inc('rlq', 341) if registers['pr'] > -6879 else do_nothing()
if registers['rlq'] > highest:
   highest = registers['rlq'] 
if 'yo' not in registers.keys(): registers['yo'] = 0 
if 'g' not in registers.keys(): registers['g'] = 0 
dec('yo', -691) if registers['g'] < -943 else do_nothing()
if registers['yo'] > highest:
   highest = registers['yo'] 
if 't' not in registers.keys(): registers['t'] = 0 
if 'afu' not in registers.keys(): registers['afu'] = 0 
inc('t', -415) if registers['afu'] <= -532 else do_nothing()
if registers['t'] > highest:
   highest = registers['t'] 
if 'afu' not in registers.keys(): registers['afu'] = 0 
if 'pr' not in registers.keys(): registers['pr'] = 0 
dec('afu', -980) if registers['pr'] == -6873 else do_nothing()
if registers['afu'] > highest:
   highest = registers['afu'] 
if 'ghj' not in registers.keys(): registers['ghj'] = 0 
if 'bfx' not in registers.keys(): registers['bfx'] = 0 
dec('ghj', 11) if registers['bfx'] != 2670 else do_nothing()
if registers['ghj'] > highest:
   highest = registers['ghj'] 
if 'afu' not in registers.keys(): registers['afu'] = 0 
if 'ghj' not in registers.keys(): registers['ghj'] = 0 
inc('afu', 873) if registers['ghj'] < -920 else do_nothing()
if registers['afu'] > highest:
   highest = registers['afu'] 
if 'k' not in registers.keys(): registers['k'] = 0 
if 'wfk' not in registers.keys(): registers['wfk'] = 0 
inc('k', 389) if registers['wfk'] != -1472 else do_nothing()
if registers['k'] > highest:
   highest = registers['k'] 
if 'u' not in registers.keys(): registers['u'] = 0 
if 'w' not in registers.keys(): registers['w'] = 0 
inc('u', 931) if registers['w'] > 1332 else do_nothing()
if registers['u'] > highest:
   highest = registers['u'] 
if 'qrc' not in registers.keys(): registers['qrc'] = 0 
if 't' not in registers.keys(): registers['t'] = 0 
dec('qrc', 565) if registers['t'] != -3958 else do_nothing()
if registers['qrc'] > highest:
   highest = registers['qrc'] 
if 'a' not in registers.keys(): registers['a'] = 0 
if 'rlq' not in registers.keys(): registers['rlq'] = 0 
inc('a', -729) if registers['rlq'] < -768 else do_nothing()
if registers['a'] > highest:
   highest = registers['a'] 
if 'sh' not in registers.keys(): registers['sh'] = 0 
if 'nkr' not in registers.keys(): registers['nkr'] = 0 
dec('sh', -345) if registers['nkr'] > -6039 else do_nothing()
if registers['sh'] > highest:
   highest = registers['sh'] 
if 'w' not in registers.keys(): registers['w'] = 0 
if 'm' not in registers.keys(): registers['m'] = 0 
inc('w', 553) if registers['m'] > 2097 else do_nothing()
if registers['w'] > highest:
   highest = registers['w'] 
if 'lpi' not in registers.keys(): registers['lpi'] = 0 
if 'qdq' not in registers.keys(): registers['qdq'] = 0 
dec('lpi', -388) if registers['qdq'] != -1755 else do_nothing()
if registers['lpi'] > highest:
   highest = registers['lpi'] 
if 'm' not in registers.keys(): registers['m'] = 0 
if 'fkp' not in registers.keys(): registers['fkp'] = 0 
dec('m', 766) if registers['fkp'] >= 4283 else do_nothing()
if registers['m'] > highest:
   highest = registers['m'] 
if 'vh' not in registers.keys(): registers['vh'] = 0 
if 'qdq' not in registers.keys(): registers['qdq'] = 0 
inc('vh', -80) if registers['qdq'] <= -1751 else do_nothing()
if registers['vh'] > highest:
   highest = registers['vh'] 
if 'g' not in registers.keys(): registers['g'] = 0 
if 'qn' not in registers.keys(): registers['qn'] = 0 
inc('g', -839) if registers['qn'] == 4252 else do_nothing()
if registers['g'] > highest:
   highest = registers['g'] 
if 'w' not in registers.keys(): registers['w'] = 0 
if 'a' not in registers.keys(): registers['a'] = 0 
dec('w', 8) if registers['a'] >= 672 else do_nothing()
if registers['w'] > highest:
   highest = registers['w'] 
if 'rlq' not in registers.keys(): registers['rlq'] = 0 
if 'a' not in registers.keys(): registers['a'] = 0 
inc('rlq', -499) if registers['a'] == 662 else do_nothing()
if registers['rlq'] > highest:
   highest = registers['rlq'] 
if 'pr' not in registers.keys(): registers['pr'] = 0 
if 'yo' not in registers.keys(): registers['yo'] = 0 
dec('pr', -627) if registers['yo'] != -2399 else do_nothing()
if registers['pr'] > highest:
   highest = registers['pr'] 
if 'm' not in registers.keys(): registers['m'] = 0 
if 'rlq' not in registers.keys(): registers['rlq'] = 0 
dec('m', -848) if registers['rlq'] < -1270 else do_nothing()
if registers['m'] > highest:
   highest = registers['m'] 
if 'vh' not in registers.keys(): registers['vh'] = 0 
if 'qn' not in registers.keys(): registers['qn'] = 0 
dec('vh', 150) if registers['qn'] > 4245 else do_nothing()
if registers['vh'] > highest:
   highest = registers['vh'] 
if 'k' not in registers.keys(): registers['k'] = 0 
if 'ghj' not in registers.keys(): registers['ghj'] = 0 
inc('k', 572) if registers['ghj'] == -922 else do_nothing()
if registers['k'] > highest:
   highest = registers['k'] 
if 'g' not in registers.keys(): registers['g'] = 0 
if 'ev' not in registers.keys(): registers['ev'] = 0 
inc('g', 953) if registers['ev'] >= -2683 else do_nothing()
if registers['g'] > highest:
   highest = registers['g'] 
if 'lpi' not in registers.keys(): registers['lpi'] = 0 
if 'fkp' not in registers.keys(): registers['fkp'] = 0 
dec('lpi', 731) if registers['fkp'] == 4287 else do_nothing()
if registers['lpi'] > highest:
   highest = registers['lpi'] 
if 'ev' not in registers.keys(): registers['ev'] = 0 
if 'qn' not in registers.keys(): registers['qn'] = 0 
dec('ev', 800) if registers['qn'] > 4247 else do_nothing()
if registers['ev'] > highest:
   highest = registers['ev'] 
if 'ev' not in registers.keys(): registers['ev'] = 0 
if 'm' not in registers.keys(): registers['m'] = 0 
inc('ev', 743) if registers['m'] < 2189 else do_nothing()
if registers['ev'] > highest:
   highest = registers['ev'] 
if 'g' not in registers.keys(): registers['g'] = 0 
if 'pr' not in registers.keys(): registers['pr'] = 0 
dec('g', 349) if registers['pr'] != -6249 else do_nothing()
if registers['g'] > highest:
   highest = registers['g'] 
if 'pr' not in registers.keys(): registers['pr'] = 0 
if 'jq' not in registers.keys(): registers['jq'] = 0 
dec('pr', -548) if registers['jq'] < 3523 else do_nothing()
if registers['pr'] > highest:
   highest = registers['pr'] 
if 'm' not in registers.keys(): registers['m'] = 0 
if 'qrc' not in registers.keys(): registers['qrc'] = 0 
inc('m', 611) if registers['qrc'] != -3073 else do_nothing()
if registers['m'] > highest:
   highest = registers['m'] 
if 'ev' not in registers.keys(): registers['ev'] = 0 
if 'k' not in registers.keys(): registers['k'] = 0 
dec('ev', -843) if registers['k'] == 2492 else do_nothing()
if registers['ev'] > highest:
   highest = registers['ev'] 
if 't' not in registers.keys(): registers['t'] = 0 
if 'vh' not in registers.keys(): registers['vh'] = 0 
inc('t', 444) if registers['vh'] != -2023 else do_nothing()
if registers['t'] > highest:
   highest = registers['t'] 
if 'qn' not in registers.keys(): registers['qn'] = 0 
if 'm' not in registers.keys(): registers['m'] = 0 
inc('qn', 101) if registers['m'] == 2183 else do_nothing()
if registers['qn'] > highest:
   highest = registers['qn'] 
if 'lpi' not in registers.keys(): registers['lpi'] = 0 
if 'pr' not in registers.keys(): registers['pr'] = 0 
dec('lpi', -749) if registers['pr'] > -5708 else do_nothing()
if registers['lpi'] > highest:
   highest = registers['lpi'] 
if 't' not in registers.keys(): registers['t'] = 0 
if 'nkr' not in registers.keys(): registers['nkr'] = 0 
inc('t', 992) if registers['nkr'] >= -6039 else do_nothing()
if registers['t'] > highest:
   highest = registers['t'] 
if 'sh' not in registers.keys(): registers['sh'] = 0 
if 'jh' not in registers.keys(): registers['jh'] = 0 
inc('sh', -859) if registers['jh'] < -2781 else do_nothing()
if registers['sh'] > highest:
   highest = registers['sh'] 
if 'sh' not in registers.keys(): registers['sh'] = 0 
if 'lpi' not in registers.keys(): registers['lpi'] = 0 
dec('sh', 456) if registers['lpi'] > -2026 else do_nothing()
if registers['sh'] > highest:
   highest = registers['sh'] 
if 'ghj' not in registers.keys(): registers['ghj'] = 0 
if 'w' not in registers.keys(): registers['w'] = 0 
inc('ghj', -765) if registers['w'] < 1883 else do_nothing()
if registers['ghj'] > highest:
   highest = registers['ghj'] 
if 'k' not in registers.keys(): registers['k'] = 0 
if 'sh' not in registers.keys(): registers['sh'] = 0 
dec('k', -268) if registers['sh'] < 682 else do_nothing()
if registers['k'] > highest:
   highest = registers['k'] 
if 'yo' not in registers.keys(): registers['yo'] = 0 
if 'sh' not in registers.keys(): registers['sh'] = 0 
inc('yo', -994) if registers['sh'] >= 669 else do_nothing()
if registers['yo'] > highest:
   highest = registers['yo'] 
if 't' not in registers.keys(): registers['t'] = 0 
if 'ev' not in registers.keys(): registers['ev'] = 0 
inc('t', -124) if registers['ev'] > -2744 else do_nothing()
if registers['t'] > highest:
   highest = registers['t'] 
if 'jh' not in registers.keys(): registers['jh'] = 0 
if 'g' not in registers.keys(): registers['g'] = 0 
inc('jh', -807) if registers['g'] < -1170 else do_nothing()
if registers['jh'] > highest:
   highest = registers['jh'] 
if 'vh' not in registers.keys(): registers['vh'] = 0 
if 'a' not in registers.keys(): registers['a'] = 0 
inc('vh', -509) if registers['a'] != 652 else do_nothing()
if registers['vh'] > highest:
   highest = registers['vh'] 
if 'ghj' not in registers.keys(): registers['ghj'] = 0 
if 'ghj' not in registers.keys(): registers['ghj'] = 0 
inc('ghj', -904) if registers['ghj'] == -913 else do_nothing()
if registers['ghj'] > highest:
   highest = registers['ghj'] 
if 'rlq' not in registers.keys(): registers['rlq'] = 0 
if 'ev' not in registers.keys(): registers['ev'] = 0 
dec('rlq', -727) if registers['ev'] > -2740 else do_nothing()
if registers['rlq'] > highest:
   highest = registers['rlq'] 
if 'vh' not in registers.keys(): registers['vh'] = 0 
if 'wfk' not in registers.keys(): registers['wfk'] = 0 
inc('vh', -752) if registers['wfk'] > -1475 else do_nothing()
if registers['vh'] > highest:
   highest = registers['vh'] 
if 'k' not in registers.keys(): registers['k'] = 0 
if 'g' not in registers.keys(): registers['g'] = 0 
inc('k', 252) if registers['g'] == -1176 else do_nothing()
if registers['k'] > highest:
   highest = registers['k'] 
if 'qrc' not in registers.keys(): registers['qrc'] = 0 
if 'g' not in registers.keys(): registers['g'] = 0 
dec('qrc', -220) if registers['g'] == -1176 else do_nothing()
if registers['qrc'] > highest:
   highest = registers['qrc'] 
if 'rlq' not in registers.keys(): registers['rlq'] = 0 
if 'afu' not in registers.keys(): registers['afu'] = 0 
inc('rlq', 850) if registers['afu'] > 1314 else do_nothing()
if registers['rlq'] > highest:
   highest = registers['rlq'] 
if 'ghj' not in registers.keys(): registers['ghj'] = 0 
if 'jh' not in registers.keys(): registers['jh'] = 0 
dec('ghj', 256) if registers['jh'] >= -3589 else do_nothing()
if registers['ghj'] > highest:
   highest = registers['ghj'] 
if 'u' not in registers.keys(): registers['u'] = 0 
if 'qdq' not in registers.keys(): registers['qdq'] = 0 
dec('u', -644) if registers['qdq'] < -1750 else do_nothing()
if registers['u'] > highest:
   highest = registers['u'] 
if 'qrc' not in registers.keys(): registers['qrc'] = 0 
if 'k' not in registers.keys(): registers['k'] = 0 
dec('qrc', -156) if registers['k'] != 3018 else do_nothing()
if registers['qrc'] > highest:
   highest = registers['qrc'] 
if 'pr' not in registers.keys(): registers['pr'] = 0 
if 'lpi' not in registers.keys(): registers['lpi'] = 0 
dec('pr', 540) if registers['lpi'] < -2013 else do_nothing()
if registers['pr'] > highest:
   highest = registers['pr'] 
if 'lpi' not in registers.keys(): registers['lpi'] = 0 
if 't' not in registers.keys(): registers['t'] = 0 
inc('lpi', -138) if registers['t'] == -3086 else do_nothing()
if registers['lpi'] > highest:
   highest = registers['lpi'] 
if 'w' not in registers.keys(): registers['w'] = 0 
if 'ev' not in registers.keys(): registers['ev'] = 0 
inc('w', -935) if registers['ev'] == -2737 else do_nothing()
if registers['w'] > highest:
   highest = registers['w'] 
if 'qn' not in registers.keys(): registers['qn'] = 0 
if 'lpi' not in registers.keys(): registers['lpi'] = 0 
inc('qn', -507) if registers['lpi'] > -2019 else do_nothing()
if registers['qn'] > highest:
   highest = registers['qn'] 
if 'qn' not in registers.keys(): registers['qn'] = 0 
if 'yo' not in registers.keys(): registers['yo'] = 0 
inc('qn', -951) if registers['yo'] == -3390 else do_nothing()
if registers['qn'] > highest:
   highest = registers['qn'] 
if 'qdq' not in registers.keys(): registers['qdq'] = 0 
if 'jh' not in registers.keys(): registers['jh'] = 0 
inc('qdq', -264) if registers['jh'] > -3591 else do_nothing()
if registers['qdq'] > highest:
   highest = registers['qdq'] 
if 'wfk' not in registers.keys(): registers['wfk'] = 0 
if 'u' not in registers.keys(): registers['u'] = 0 
dec('wfk', -87) if registers['u'] > -965 else do_nothing()
if registers['wfk'] > highest:
   highest = registers['wfk'] 
if 'qn' not in registers.keys(): registers['qn'] = 0 
if 'nkr' not in registers.keys(): registers['nkr'] = 0 
dec('qn', -130) if registers['nkr'] < -6029 else do_nothing()
if registers['qn'] > highest:
   highest = registers['qn'] 
if 'g' not in registers.keys(): registers['g'] = 0 
if 't' not in registers.keys(): registers['t'] = 0 
inc('g', -245) if registers['t'] != -3076 else do_nothing()
if registers['g'] > highest:
   highest = registers['g'] 
if 'jq' not in registers.keys(): registers['jq'] = 0 
if 'qdq' not in registers.keys(): registers['qdq'] = 0 
inc('jq', 992) if registers['qdq'] < -2013 else do_nothing()
if registers['jq'] > highest:
   highest = registers['jq'] 
if 'wfk' not in registers.keys(): registers['wfk'] = 0 
if 'g' not in registers.keys(): registers['g'] = 0 
inc('wfk', 169) if registers['g'] <= -1416 else do_nothing()
if registers['wfk'] > highest:
   highest = registers['wfk'] 
if 'm' not in registers.keys(): registers['m'] = 0 
if 'qdq' not in registers.keys(): registers['qdq'] = 0 
dec('m', -822) if registers['qdq'] != -2016 else do_nothing()
if registers['m'] > highest:
   highest = registers['m'] 
if 'vh' not in registers.keys(): registers['vh'] = 0 
if 'pr' not in registers.keys(): registers['pr'] = 0 
dec('vh', -900) if registers['pr'] > -6233 else do_nothing()
if registers['vh'] > highest:
   highest = registers['vh'] 
if 'ghj' not in registers.keys(): registers['ghj'] = 0 
if 'sh' not in registers.keys(): registers['sh'] = 0 
inc('ghj', -57) if registers['sh'] >= 670 else do_nothing()
if registers['ghj'] > highest:
   highest = registers['ghj'] 
if 'ev' not in registers.keys(): registers['ev'] = 0 
if 'pr' not in registers.keys(): registers['pr'] = 0 
dec('ev', -617) if registers['pr'] <= -6229 else do_nothing()
if registers['ev'] > highest:
   highest = registers['ev'] 
if 't' not in registers.keys(): registers['t'] = 0 
if 'w' not in registers.keys(): registers['w'] = 0 
inc('t', -284) if registers['w'] != 958 else do_nothing()
if registers['t'] > highest:
   highest = registers['t'] 
if 'fkp' not in registers.keys(): registers['fkp'] = 0 
if 'sh' not in registers.keys(): registers['sh'] = 0 
dec('fkp', 148) if registers['sh'] > 664 else do_nothing()
if registers['fkp'] > highest:
   highest = registers['fkp'] 
if 'jq' not in registers.keys(): registers['jq'] = 0 
if 'yo' not in registers.keys(): registers['yo'] = 0 
dec('jq', 813) if registers['yo'] < -3385 else do_nothing()
if registers['jq'] > highest:
   highest = registers['jq'] 
if 'sh' not in registers.keys(): registers['sh'] = 0 
if 'm' not in registers.keys(): registers['m'] = 0 
inc('sh', 582) if registers['m'] >= 2181 else do_nothing()
if registers['sh'] > highest:
   highest = registers['sh'] 
if 'k' not in registers.keys(): registers['k'] = 0 
if 'vh' not in registers.keys(): registers['vh'] = 0 
inc('k', -737) if registers['vh'] == -3284 else do_nothing()
if registers['k'] > highest:
   highest = registers['k'] 
if 'rlq' not in registers.keys(): registers['rlq'] = 0 
if 'sh' not in registers.keys(): registers['sh'] = 0 
dec('rlq', 133) if registers['sh'] < 1250 else do_nothing()
if registers['rlq'] > highest:
   highest = registers['rlq'] 
if 'nkr' not in registers.keys(): registers['nkr'] = 0 
if 'ev' not in registers.keys(): registers['ev'] = 0 
dec('nkr', 990) if registers['ev'] < -2114 else do_nothing()
if registers['nkr'] > highest:
   highest = registers['nkr'] 
if 'lpi' not in registers.keys(): registers['lpi'] = 0 
if 'jh' not in registers.keys(): registers['jh'] = 0 
dec('lpi', 144) if registers['jh'] < -3574 else do_nothing()
if registers['lpi'] > highest:
   highest = registers['lpi'] 
if 'a' not in registers.keys(): registers['a'] = 0 
if 'rlq' not in registers.keys(): registers['rlq'] = 0 
dec('a', -303) if registers['rlq'] <= 302 else do_nothing()
if registers['a'] > highest:
   highest = registers['a'] 
if 'qdq' not in registers.keys(): registers['qdq'] = 0 
if 'jh' not in registers.keys(): registers['jh'] = 0 
inc('qdq', 140) if registers['jh'] == -3583 else do_nothing()
if registers['qdq'] > highest:
   highest = registers['qdq'] 
if 'wfk' not in registers.keys(): registers['wfk'] = 0 
if 'qn' not in registers.keys(): registers['qn'] = 0 
dec('wfk', -274) if registers['qn'] != 3976 else do_nothing()
if registers['wfk'] > highest:
   highest = registers['wfk'] 
if 'qrc' not in registers.keys(): registers['qrc'] = 0 
if 'ev' not in registers.keys(): registers['ev'] = 0 
dec('qrc', 982) if registers['ev'] > -2129 else do_nothing()
if registers['qrc'] > highest:
   highest = registers['qrc'] 
if 'a' not in registers.keys(): registers['a'] = 0 
if 'a' not in registers.keys(): registers['a'] = 0 
dec('a', 118) if registers['a'] <= 956 else do_nothing()
if registers['a'] > highest:
   highest = registers['a'] 
if 'bfx' not in registers.keys(): registers['bfx'] = 0 
if 'k' not in registers.keys(): registers['k'] = 0 
inc('bfx', 302) if registers['k'] >= 2263 else do_nothing()
if registers['bfx'] > highest:
   highest = registers['bfx'] 
if 'rlq' not in registers.keys(): registers['rlq'] = 0 
if 'ghj' not in registers.keys(): registers['ghj'] = 0 
dec('rlq', 286) if registers['ghj'] != -1238 else do_nothing()
if registers['rlq'] > highest:
   highest = registers['rlq'] 
if 'vh' not in registers.keys(): registers['vh'] = 0 
if 'nkr' not in registers.keys(): registers['nkr'] = 0 
inc('vh', -79) if registers['nkr'] <= -7017 else do_nothing()
if registers['vh'] > highest:
   highest = registers['vh'] 
if 'm' not in registers.keys(): registers['m'] = 0 
if 'u' not in registers.keys(): registers['u'] = 0 
dec('m', -151) if registers['u'] > -972 else do_nothing()
if registers['m'] > highest:
   highest = registers['m'] 
if 'jh' not in registers.keys(): registers['jh'] = 0 
if 'w' not in registers.keys(): registers['w'] = 0 
dec('jh', -165) if registers['w'] == 953 else do_nothing()
if registers['jh'] > highest:
   highest = registers['jh'] 
if 'fkp' not in registers.keys(): registers['fkp'] = 0 
if 'fkp' not in registers.keys(): registers['fkp'] = 0 
inc('fkp', -879) if registers['fkp'] != 4129 else do_nothing()
if registers['fkp'] > highest:
   highest = registers['fkp'] 
if 't' not in registers.keys(): registers['t'] = 0 
if 'fkp' not in registers.keys(): registers['fkp'] = 0 
dec('t', -926) if registers['fkp'] >= 3267 else do_nothing()
if registers['t'] > highest:
   highest = registers['t'] 
if 'rlq' not in registers.keys(): registers['rlq'] = 0 
if 'rlq' not in registers.keys(): registers['rlq'] = 0 
inc('rlq', 659) if registers['rlq'] > 14 else do_nothing()
if registers['rlq'] > highest:
   highest = registers['rlq'] 
if 'qrc' not in registers.keys(): registers['qrc'] = 0 
if 'bfx' not in registers.keys(): registers['bfx'] = 0 
dec('qrc', -879) if registers['bfx'] <= 2977 else do_nothing()
if registers['qrc'] > highest:
   highest = registers['qrc'] 
if 'pr' not in registers.keys(): registers['pr'] = 0 
if 'fkp' not in registers.keys(): registers['fkp'] = 0 
dec('pr', -568) if registers['fkp'] <= 3265 else do_nothing()
if registers['pr'] > highest:
   highest = registers['pr'] 
if 'ghj' not in registers.keys(): registers['ghj'] = 0 
if 't' not in registers.keys(): registers['t'] = 0 
dec('ghj', 941) if registers['t'] == -3367 else do_nothing()
if registers['ghj'] > highest:
   highest = registers['ghj'] 
if 'm' not in registers.keys(): registers['m'] = 0 
if 'jh' not in registers.keys(): registers['jh'] = 0 
inc('m', 852) if registers['jh'] <= -3411 else do_nothing()
if registers['m'] > highest:
   highest = registers['m'] 
if 'k' not in registers.keys(): registers['k'] = 0 
if 'nkr' not in registers.keys(): registers['nkr'] = 0 
inc('k', 781) if registers['nkr'] == -7024 else do_nothing()
if registers['k'] > highest:
   highest = registers['k'] 
if 'fkp' not in registers.keys(): registers['fkp'] = 0 
if 'rlq' not in registers.keys(): registers['rlq'] = 0 
dec('fkp', -731) if registers['rlq'] < 681 else do_nothing()
if registers['fkp'] > highest:
   highest = registers['fkp'] 
if 'w' not in registers.keys(): registers['w'] = 0 
if 'u' not in registers.keys(): registers['u'] = 0 
inc('w', -147) if registers['u'] == -957 else do_nothing()
if registers['w'] > highest:
   highest = registers['w'] 
if 'vh' not in registers.keys(): registers['vh'] = 0 
if 'k' not in registers.keys(): registers['k'] = 0 
inc('vh', 928) if registers['k'] == 3052 else do_nothing()
if registers['vh'] > highest:
   highest = registers['vh'] 
if 't' not in registers.keys(): registers['t'] = 0 
if 'qdq' not in registers.keys(): registers['qdq'] = 0 
inc('t', -993) if registers['qdq'] != -2015 else do_nothing()
if registers['t'] > highest:
   highest = registers['t'] 
if 'u' not in registers.keys(): registers['u'] = 0 
if 'wfk' not in registers.keys(): registers['wfk'] = 0 
inc('u', 920) if registers['wfk'] != -1216 else do_nothing()
if registers['u'] > highest:
   highest = registers['u'] 
if 'qrc' not in registers.keys(): registers['qrc'] = 0 
if 'pr' not in registers.keys(): registers['pr'] = 0 
dec('qrc', -891) if registers['pr'] != -5673 else do_nothing()
if registers['qrc'] > highest:
   highest = registers['qrc'] 
if 'rlq' not in registers.keys(): registers['rlq'] = 0 
if 'fkp' not in registers.keys(): registers['fkp'] = 0 
inc('rlq', 195) if registers['fkp'] > 3985 else do_nothing()
if registers['rlq'] > highest:
   highest = registers['rlq'] 
if 'jq' not in registers.keys(): registers['jq'] = 0 
if 'rlq' not in registers.keys(): registers['rlq'] = 0 
dec('jq', 837) if registers['rlq'] >= 861 else do_nothing()
if registers['jq'] > highest:
   highest = registers['jq'] 
if 'nkr' not in registers.keys(): registers['nkr'] = 0 
if 'pr' not in registers.keys(): registers['pr'] = 0 
inc('nkr', -784) if registers['pr'] == -5670 else do_nothing()
if registers['nkr'] > highest:
   highest = registers['nkr'] 
if 'u' not in registers.keys(): registers['u'] = 0 
if 'w' not in registers.keys(): registers['w'] = 0 
inc('u', 873) if registers['w'] < 963 else do_nothing()
if registers['u'] > highest:
   highest = registers['u'] 
if 't' not in registers.keys(): registers['t'] = 0 
if 'rlq' not in registers.keys(): registers['rlq'] = 0 
dec('t', -903) if registers['rlq'] == 870 else do_nothing()
if registers['t'] > highest:
   highest = registers['t'] 
if 'qn' not in registers.keys(): registers['qn'] = 0 
if 'jq' not in registers.keys(): registers['jq'] = 0 
inc('qn', 751) if registers['jq'] != 2851 else do_nothing()
if registers['qn'] > highest:
   highest = registers['qn'] 
if 'jh' not in registers.keys(): registers['jh'] = 0 
if 'bfx' not in registers.keys(): registers['bfx'] = 0 
inc('jh', 591) if registers['bfx'] != 2971 else do_nothing()
if registers['jh'] > highest:
   highest = registers['jh'] 
if 'wfk' not in registers.keys(): registers['wfk'] = 0 
if 'm' not in registers.keys(): registers['m'] = 0 
dec('wfk', -608) if registers['m'] < 3187 else do_nothing()
if registers['wfk'] > highest:
   highest = registers['wfk'] 
if 'rlq' not in registers.keys(): registers['rlq'] = 0 
if 'qdq' not in registers.keys(): registers['qdq'] = 0 
inc('rlq', 16) if registers['qdq'] != -2012 else do_nothing()
if registers['rlq'] > highest:
   highest = registers['rlq'] 
if 'qn' not in registers.keys(): registers['qn'] = 0 
if 't' not in registers.keys(): registers['t'] = 0 
inc('qn', -188) if registers['t'] <= -3452 else do_nothing()
if registers['qn'] > highest:
   highest = registers['qn'] 
if 'vh' not in registers.keys(): registers['vh'] = 0 
if 'm' not in registers.keys(): registers['m'] = 0 
inc('vh', -24) if registers['m'] < 3187 else do_nothing()
if registers['vh'] > highest:
   highest = registers['vh'] 
if 'ev' not in registers.keys(): registers['ev'] = 0 
if 'rlq' not in registers.keys(): registers['rlq'] = 0 
dec('ev', -614) if registers['rlq'] < 888 else do_nothing()
if registers['ev'] > highest:
   highest = registers['ev'] 
if 'a' not in registers.keys(): registers['a'] = 0 
if 'qdq' not in registers.keys(): registers['qdq'] = 0 
inc('a', -889) if registers['qdq'] <= -2014 else do_nothing()
if registers['a'] > highest:
   highest = registers['a'] 
if 'qn' not in registers.keys(): registers['qn'] = 0 
if 'm' not in registers.keys(): registers['m'] = 0 
dec('qn', -268) if registers['m'] < 3189 else do_nothing()
if registers['qn'] > highest:
   highest = registers['qn'] 
if 'yo' not in registers.keys(): registers['yo'] = 0 
if 'afu' not in registers.keys(): registers['afu'] = 0 
dec('yo', 881) if registers['afu'] <= 1319 else do_nothing()
if registers['yo'] > highest:
   highest = registers['yo'] 
if 'rlq' not in registers.keys(): registers['rlq'] = 0 
if 'qdq' not in registers.keys(): registers['qdq'] = 0 
inc('rlq', -157) if registers['qdq'] < -2006 else do_nothing()
if registers['rlq'] > highest:
   highest = registers['rlq'] 
if 'pr' not in registers.keys(): registers['pr'] = 0 
if 'afu' not in registers.keys(): registers['afu'] = 0 
dec('pr', -159) if registers['afu'] >= 1311 else do_nothing()
if registers['pr'] > highest:
   highest = registers['pr'] 
if 'ev' not in registers.keys(): registers['ev'] = 0 
if 'fkp' not in registers.keys(): registers['fkp'] = 0 
dec('ev', 780) if registers['fkp'] == 3990 else do_nothing()
if registers['ev'] > highest:
   highest = registers['ev'] 
if 'yo' not in registers.keys(): registers['yo'] = 0 
if 'bfx' not in registers.keys(): registers['bfx'] = 0 
dec('yo', -893) if registers['bfx'] <= 2974 else do_nothing()
if registers['yo'] > highest:
   highest = registers['yo'] 
if 'w' not in registers.keys(): registers['w'] = 0 
if 'm' not in registers.keys(): registers['m'] = 0 
inc('w', 62) if registers['m'] <= 3189 else do_nothing()
if registers['w'] > highest:
   highest = registers['w'] 
if 'w' not in registers.keys(): registers['w'] = 0 
if 'qdq' not in registers.keys(): registers['qdq'] = 0 
inc('w', 876) if registers['qdq'] == -2016 else do_nothing()
if registers['w'] > highest:
   highest = registers['w'] 
if 'w' not in registers.keys(): registers['w'] = 0 
if 'g' not in registers.keys(): registers['g'] = 0 
inc('w', -860) if registers['g'] >= -1426 else do_nothing()
if registers['w'] > highest:
   highest = registers['w'] 
if 't' not in registers.keys(): registers['t'] = 0 
if 'lpi' not in registers.keys(): registers['lpi'] = 0 
dec('t', -819) if registers['lpi'] < -2167 else do_nothing()
if registers['t'] > highest:
   highest = registers['t'] 
if 'g' not in registers.keys(): registers['g'] = 0 
if 'ghj' not in registers.keys(): registers['ghj'] = 0 
inc('g', -258) if registers['ghj'] != -2184 else do_nothing()
if registers['g'] > highest:
   highest = registers['g'] 
if 'bfx' not in registers.keys(): registers['bfx'] = 0 
if 'ghj' not in registers.keys(): registers['ghj'] = 0 
dec('bfx', -116) if registers['ghj'] > -2184 else do_nothing()
if registers['bfx'] > highest:
   highest = registers['bfx'] 
if 'yo' not in registers.keys(): registers['yo'] = 0 
if 'm' not in registers.keys(): registers['m'] = 0 
inc('yo', -995) if registers['m'] >= 3182 else do_nothing()
if registers['yo'] > highest:
   highest = registers['yo'] 
if 'vh' not in registers.keys(): registers['vh'] = 0 
if 'vh' not in registers.keys(): registers['vh'] = 0 
dec('vh', -479) if registers['vh'] == -2459 else do_nothing()
if registers['vh'] > highest:
   highest = registers['vh'] 
if 'g' not in registers.keys(): registers['g'] = 0 
if 'yo' not in registers.keys(): registers['yo'] = 0 
inc('g', 896) if registers['yo'] == -4369 else do_nothing()
if registers['g'] > highest:
   highest = registers['g'] 
if 'ghj' not in registers.keys(): registers['ghj'] = 0 
if 'w' not in registers.keys(): registers['w'] = 0 
inc('ghj', -594) if registers['w'] < 1029 else do_nothing()
if registers['ghj'] > highest:
   highest = registers['ghj'] 
if 'jh' not in registers.keys(): registers['jh'] = 0 
if 'g' not in registers.keys(): registers['g'] = 0 
dec('jh', -204) if registers['g'] > -786 else do_nothing()
if registers['jh'] > highest:
   highest = registers['jh'] 
if 'jh' not in registers.keys(): registers['jh'] = 0 
if 'rlq' not in registers.keys(): registers['rlq'] = 0 
inc('jh', -320) if registers['rlq'] >= 729 else do_nothing()
if registers['jh'] > highest:
   highest = registers['jh'] 
if 'wfk' not in registers.keys(): registers['wfk'] = 0 
if 'u' not in registers.keys(): registers['u'] = 0 
inc('wfk', 699) if registers['u'] < 840 else do_nothing()
if registers['wfk'] > highest:
   highest = registers['wfk'] 
if 'nkr' not in registers.keys(): registers['nkr'] = 0 
if 'sh' not in registers.keys(): registers['sh'] = 0 
dec('nkr', -785) if registers['sh'] < 1248 else do_nothing()
if registers['nkr'] > highest:
   highest = registers['nkr'] 
if 'ev' not in registers.keys(): registers['ev'] = 0 
if 'k' not in registers.keys(): registers['k'] = 0 
inc('ev', -21) if registers['k'] <= 3061 else do_nothing()
if registers['ev'] > highest:
   highest = registers['ev'] 
if 'k' not in registers.keys(): registers['k'] = 0 
if 'jq' not in registers.keys(): registers['jq'] = 0 
dec('k', -540) if registers['jq'] >= 2860 else do_nothing()
if registers['k'] > highest:
   highest = registers['k'] 
if 'a' not in registers.keys(): registers['a'] = 0 
if 'a' not in registers.keys(): registers['a'] = 0 
dec('a', 282) if registers['a'] != 76 else do_nothing()
if registers['a'] > highest:
   highest = registers['a'] 
if 'ev' not in registers.keys(): registers['ev'] = 0 
if 'fkp' not in registers.keys(): registers['fkp'] = 0 
dec('ev', 320) if registers['fkp'] == 3990 else do_nothing()
if registers['ev'] > highest:
   highest = registers['ev'] 
if 'ghj' not in registers.keys(): registers['ghj'] = 0 
if 'k' not in registers.keys(): registers['k'] = 0 
dec('ghj', -655) if registers['k'] != 3588 else do_nothing()
if registers['ghj'] > highest:
   highest = registers['ghj'] 
if 'nkr' not in registers.keys(): registers['nkr'] = 0 
if 'sh' not in registers.keys(): registers['sh'] = 0 
inc('nkr', 31) if registers['sh'] < 1263 else do_nothing()
if registers['nkr'] > highest:
   highest = registers['nkr'] 
if 'qrc' not in registers.keys(): registers['qrc'] = 0 
if 'qn' not in registers.keys(): registers['qn'] = 0 
dec('qrc', 182) if registers['qn'] != 4807 else do_nothing()
if registers['qrc'] > highest:
   highest = registers['qrc'] 
if 'wfk' not in registers.keys(): registers['wfk'] = 0 
if 'k' not in registers.keys(): registers['k'] = 0 
dec('wfk', 453) if registers['k'] > 3590 else do_nothing()
if registers['wfk'] > highest:
   highest = registers['wfk'] 
if 'fkp' not in registers.keys(): registers['fkp'] = 0 
if 'yo' not in registers.keys(): registers['yo'] = 0 
inc('fkp', -535) if registers['yo'] >= -4376 else do_nothing()
if registers['fkp'] > highest:
   highest = registers['fkp'] 
if 'qn' not in registers.keys(): registers['qn'] = 0 
if 'rlq' not in registers.keys(): registers['rlq'] = 0 
inc('qn', -304) if registers['rlq'] == 729 else do_nothing()
if registers['qn'] > highest:
   highest = registers['qn'] 
if 'jh' not in registers.keys(): registers['jh'] = 0 
if 't' not in registers.keys(): registers['t'] = 0 
inc('jh', 46) if registers['t'] != -3453 else do_nothing()
if registers['jh'] > highest:
   highest = registers['jh'] 
if 'rlq' not in registers.keys(): registers['rlq'] = 0 
if 'bfx' not in registers.keys(): registers['bfx'] = 0 
dec('rlq', -90) if registers['bfx'] == 3085 else do_nothing()
if registers['rlq'] > highest:
   highest = registers['rlq'] 
if 'u' not in registers.keys(): registers['u'] = 0 
if 'm' not in registers.keys(): registers['m'] = 0 
inc('u', -448) if registers['m'] == 3186 else do_nothing()
if registers['u'] > highest:
   highest = registers['u'] 
if 'bfx' not in registers.keys(): registers['bfx'] = 0 
if 'jq' not in registers.keys(): registers['jq'] = 0 
inc('bfx', -855) if registers['jq'] == 2860 else do_nothing()
if registers['bfx'] > highest:
   highest = registers['bfx'] 
if 'lpi' not in registers.keys(): registers['lpi'] = 0 
if 'bfx' not in registers.keys(): registers['bfx'] = 0 
inc('lpi', 574) if registers['bfx'] < 2231 else do_nothing()
if registers['lpi'] > highest:
   highest = registers['lpi'] 
if 'qdq' not in registers.keys(): registers['qdq'] = 0 
if 'vh' not in registers.keys(): registers['vh'] = 0 
dec('qdq', -247) if registers['vh'] < -1974 else do_nothing()
if registers['qdq'] > highest:
   highest = registers['qdq'] 
if 'pr' not in registers.keys(): registers['pr'] = 0 
if 'qrc' not in registers.keys(): registers['qrc'] = 0 
dec('pr', 795) if registers['qrc'] <= -1911 else do_nothing()
if registers['pr'] > highest:
   highest = registers['pr'] 
if 'rlq' not in registers.keys(): registers['rlq'] = 0 
if 'u' not in registers.keys(): registers['u'] = 0 
dec('rlq', -363) if registers['u'] == 382 else do_nothing()
if registers['rlq'] > highest:
   highest = registers['rlq'] 
if 'wfk' not in registers.keys(): registers['wfk'] = 0 
if 'g' not in registers.keys(): registers['g'] = 0 
dec('wfk', 924) if registers['g'] >= -780 else do_nothing()
if registers['wfk'] > highest:
   highest = registers['wfk'] 
if 'u' not in registers.keys(): registers['u'] = 0 
if 'lpi' not in registers.keys(): registers['lpi'] = 0 
inc('u', 883) if registers['lpi'] >= -1593 else do_nothing()
if registers['u'] > highest:
   highest = registers['u'] 
if 'w' not in registers.keys(): registers['w'] = 0 
if 'ghj' not in registers.keys(): registers['ghj'] = 0 
inc('w', 819) if registers['ghj'] == -1521 else do_nothing()
if registers['w'] > highest:
   highest = registers['w'] 
if 'sh' not in registers.keys(): registers['sh'] = 0 
if 'lpi' not in registers.keys(): registers['lpi'] = 0 
dec('sh', 299) if registers['lpi'] > -1593 else do_nothing()
if registers['sh'] > highest:
   highest = registers['sh'] 
if 'bfx' not in registers.keys(): registers['bfx'] = 0 
if 'a' not in registers.keys(): registers['a'] = 0 
dec('bfx', 677) if registers['a'] != 76 else do_nothing()
if registers['bfx'] > highest:
   highest = registers['bfx'] 
if 'lpi' not in registers.keys(): registers['lpi'] = 0 
if 'fkp' not in registers.keys(): registers['fkp'] = 0 
dec('lpi', -513) if registers['fkp'] > 3447 else do_nothing()
if registers['lpi'] > highest:
   highest = registers['lpi'] 
if 'ghj' not in registers.keys(): registers['ghj'] = 0 
if 'w' not in registers.keys(): registers['w'] = 0 
dec('ghj', 149) if registers['w'] > 1841 else do_nothing()
if registers['ghj'] > highest:
   highest = registers['ghj'] 
if 'rlq' not in registers.keys(): registers['rlq'] = 0 
if 'fkp' not in registers.keys(): registers['fkp'] = 0 
dec('rlq', 760) if registers['fkp'] == 3456 else do_nothing()
if registers['rlq'] > highest:
   highest = registers['rlq'] 
if 'jh' not in registers.keys(): registers['jh'] = 0 
if 'vh' not in registers.keys(): registers['vh'] = 0 
inc('jh', -371) if registers['vh'] == -1980 else do_nothing()
if registers['jh'] > highest:
   highest = registers['jh'] 
if 'fkp' not in registers.keys(): registers['fkp'] = 0 
if 'w' not in registers.keys(): registers['w'] = 0 
inc('fkp', -613) if registers['w'] < 1851 else do_nothing()
if registers['fkp'] > highest:
   highest = registers['fkp'] 
if 'ev' not in registers.keys(): registers['ev'] = 0 
if 'qrc' not in registers.keys(): registers['qrc'] = 0 
inc('ev', -657) if registers['qrc'] != -1912 else do_nothing()
if registers['ev'] > highest:
   highest = registers['ev'] 
if 'qdq' not in registers.keys(): registers['qdq'] = 0 
if 'k' not in registers.keys(): registers['k'] = 0 
inc('qdq', -594) if registers['k'] < 3597 else do_nothing()
if registers['qdq'] > highest:
   highest = registers['qdq'] 
if 'fkp' not in registers.keys(): registers['fkp'] = 0 
if 'qdq' not in registers.keys(): registers['qdq'] = 0 
inc('fkp', -974) if registers['qdq'] < -2354 else do_nothing()
if registers['fkp'] > highest:
   highest = registers['fkp'] 
if 'fkp' not in registers.keys(): registers['fkp'] = 0 
if 'jq' not in registers.keys(): registers['jq'] = 0 
dec('fkp', -797) if registers['jq'] >= 2870 else do_nothing()
if registers['fkp'] > highest:
   highest = registers['fkp'] 
if 'jh' not in registers.keys(): registers['jh'] = 0 
if 'sh' not in registers.keys(): registers['sh'] = 0 
dec('jh', 131) if registers['sh'] <= 957 else do_nothing()
if registers['jh'] > highest:
   highest = registers['jh'] 
if 'lpi' not in registers.keys(): registers['lpi'] = 0 
if 'fkp' not in registers.keys(): registers['fkp'] = 0 
dec('lpi', 350) if registers['fkp'] >= 1861 else do_nothing()
if registers['lpi'] > highest:
   highest = registers['lpi'] 
if 'ghj' not in registers.keys(): registers['ghj'] = 0 
if 'afu' not in registers.keys(): registers['afu'] = 0 
dec('ghj', -888) if registers['afu'] != 1312 else do_nothing()
if registers['ghj'] > highest:
   highest = registers['ghj'] 
if 'rlq' not in registers.keys(): registers['rlq'] = 0 
if 'jq' not in registers.keys(): registers['jq'] = 0 
inc('rlq', 43) if registers['jq'] >= 2859 else do_nothing()
if registers['rlq'] > highest:
   highest = registers['rlq'] 
if 'u' not in registers.keys(): registers['u'] = 0 
if 'a' not in registers.keys(): registers['a'] = 0 
inc('u', 604) if registers['a'] > 69 else do_nothing()
if registers['u'] > highest:
   highest = registers['u'] 
if 'jq' not in registers.keys(): registers['jq'] = 0 
if 'qrc' not in registers.keys(): registers['qrc'] = 0 
inc('jq', -490) if registers['qrc'] != -1909 else do_nothing()
if registers['jq'] > highest:
   highest = registers['jq'] 
if 'w' not in registers.keys(): registers['w'] = 0 
if 'a' not in registers.keys(): registers['a'] = 0 
inc('w', -816) if registers['a'] >= 74 else do_nothing()
if registers['w'] > highest:
   highest = registers['w'] 
if 'afu' not in registers.keys(): registers['afu'] = 0 
if 'rlq' not in registers.keys(): registers['rlq'] = 0 
inc('afu', 3) if registers['rlq'] > 467 else do_nothing()
if registers['afu'] > highest:
   highest = registers['afu'] 
if 'yo' not in registers.keys(): registers['yo'] = 0 
if 'jq' not in registers.keys(): registers['jq'] = 0 
dec('yo', 688) if registers['jq'] <= 2866 else do_nothing()
if registers['yo'] > highest:
   highest = registers['yo'] 
if 'jh' not in registers.keys(): registers['jh'] = 0 
if 'qn' not in registers.keys(): registers['qn'] = 0 
dec('jh', 134) if registers['qn'] < 4506 else do_nothing()
if registers['jh'] > highest:
   highest = registers['jh'] 
if 'afu' not in registers.keys(): registers['afu'] = 0 
if 'ghj' not in registers.keys(): registers['ghj'] = 0 
dec('afu', -838) if registers['ghj'] > -788 else do_nothing()
if registers['afu'] > highest:
   highest = registers['afu'] 
if 'g' not in registers.keys(): registers['g'] = 0 
if 'qn' not in registers.keys(): registers['qn'] = 0 
inc('g', -201) if registers['qn'] < 4507 else do_nothing()
if registers['g'] > highest:
   highest = registers['g'] 
if 'qn' not in registers.keys(): registers['qn'] = 0 
if 'm' not in registers.keys(): registers['m'] = 0 
inc('qn', 216) if registers['m'] <= 3188 else do_nothing()
if registers['qn'] > highest:
   highest = registers['qn'] 
if 'qdq' not in registers.keys(): registers['qdq'] = 0 
if 'qn' not in registers.keys(): registers['qn'] = 0 
inc('qdq', -311) if registers['qn'] < 4729 else do_nothing()
if registers['qdq'] > highest:
   highest = registers['qdq'] 
if 'qrc' not in registers.keys(): registers['qrc'] = 0 
if 'fkp' not in registers.keys(): registers['fkp'] = 0 
inc('qrc', -418) if registers['fkp'] > 1860 else do_nothing()
if registers['qrc'] > highest:
   highest = registers['qrc'] 
if 'yo' not in registers.keys(): registers['yo'] = 0 
if 'qrc' not in registers.keys(): registers['qrc'] = 0 
dec('yo', 109) if registers['qrc'] <= -2326 else do_nothing()
if registers['yo'] > highest:
   highest = registers['yo'] 
if 'qrc' not in registers.keys(): registers['qrc'] = 0 
if 'jq' not in registers.keys(): registers['jq'] = 0 
dec('qrc', 29) if registers['jq'] == 2854 else do_nothing()
if registers['qrc'] > highest:
   highest = registers['qrc'] 
if 'yo' not in registers.keys(): registers['yo'] = 0 
if 'm' not in registers.keys(): registers['m'] = 0 
inc('yo', -110) if registers['m'] <= 3187 else do_nothing()
if registers['yo'] > highest:
   highest = registers['yo'] 
if 'k' not in registers.keys(): registers['k'] = 0 
if 'wfk' not in registers.keys(): registers['wfk'] = 0 
inc('k', 80) if registers['wfk'] == -355 else do_nothing()
if registers['k'] > highest:
   highest = registers['k'] 
if 'ghj' not in registers.keys(): registers['ghj'] = 0 
if 'ghj' not in registers.keys(): registers['ghj'] = 0 
inc('ghj', -195) if registers['ghj'] > -788 else do_nothing()
if registers['ghj'] > highest:
   highest = registers['ghj'] 
if 'lpi' not in registers.keys(): registers['lpi'] = 0 
if 'w' not in registers.keys(): registers['w'] = 0 
dec('lpi', 758) if registers['w'] != 1044 else do_nothing()
if registers['lpi'] > highest:
   highest = registers['lpi'] 
if 'jh' not in registers.keys(): registers['jh'] = 0 
if 'fkp' not in registers.keys(): registers['fkp'] = 0 
dec('jh', -573) if registers['fkp'] >= 1866 else do_nothing()
if registers['jh'] > highest:
   highest = registers['jh'] 
if 'rlq' not in registers.keys(): registers['rlq'] = 0 
if 'qrc' not in registers.keys(): registers['qrc'] = 0 
inc('rlq', 35) if registers['qrc'] == -2327 else do_nothing()
if registers['rlq'] > highest:
   highest = registers['rlq'] 
if 'pr' not in registers.keys(): registers['pr'] = 0 
if 'lpi' not in registers.keys(): registers['lpi'] = 0 
dec('pr', -990) if registers['lpi'] <= -2175 else do_nothing()
if registers['pr'] > highest:
   highest = registers['pr'] 
if 'wfk' not in registers.keys(): registers['wfk'] = 0 
if 'vh' not in registers.keys(): registers['vh'] = 0 
inc('wfk', -456) if registers['vh'] > -1985 else do_nothing()
if registers['wfk'] > highest:
   highest = registers['wfk'] 
if 'rlq' not in registers.keys(): registers['rlq'] = 0 
if 'a' not in registers.keys(): registers['a'] = 0 
inc('rlq', 631) if registers['a'] > 72 else do_nothing()
if registers['rlq'] > highest:
   highest = registers['rlq'] 
if 'yo' not in registers.keys(): registers['yo'] = 0 
if 'k' not in registers.keys(): registers['k'] = 0 
inc('yo', 116) if registers['k'] <= 3678 else do_nothing()
if registers['yo'] > highest:
   highest = registers['yo'] 
if 'g' not in registers.keys(): registers['g'] = 0 
if 'qdq' not in registers.keys(): registers['qdq'] = 0 
inc('g', 85) if registers['qdq'] <= -2667 else do_nothing()
if registers['g'] > highest:
   highest = registers['g'] 
if 'ev' not in registers.keys(): registers['ev'] = 0 
if 'g' not in registers.keys(): registers['g'] = 0 
dec('ev', -75) if registers['g'] >= -903 else do_nothing()
if registers['ev'] > highest:
   highest = registers['ev'] 
if 'ev' not in registers.keys(): registers['ev'] = 0 
if 'lpi' not in registers.keys(): registers['lpi'] = 0 
dec('ev', -646) if registers['lpi'] > -2184 else do_nothing()
if registers['ev'] > highest:
   highest = registers['ev'] 
if 'nkr' not in registers.keys(): registers['nkr'] = 0 
if 'afu' not in registers.keys(): registers['afu'] = 0 
dec('nkr', 870) if registers['afu'] > 2154 else do_nothing()
if registers['nkr'] > highest:
   highest = registers['nkr'] 
if 'jq' not in registers.keys(): registers['jq'] = 0 
if 'm' not in registers.keys(): registers['m'] = 0 
inc('jq', -53) if registers['m'] < 3189 else do_nothing()
if registers['jq'] > highest:
   highest = registers['jq'] 
if 'afu' not in registers.keys(): registers['afu'] = 0 
if 'nkr' not in registers.keys(): registers['nkr'] = 0 
dec('afu', 611) if registers['nkr'] < -8646 else do_nothing()
if registers['afu'] > highest:
   highest = registers['afu'] 
if 'm' not in registers.keys(): registers['m'] = 0 
if 'g' not in registers.keys(): registers['g'] = 0 
dec('m', -287) if registers['g'] < -897 else do_nothing()
if registers['m'] > highest:
   highest = registers['m'] 
if 'nkr' not in registers.keys(): registers['nkr'] = 0 
if 'a' not in registers.keys(): registers['a'] = 0 
inc('nkr', 36) if registers['a'] < 85 else do_nothing()
if registers['nkr'] > highest:
   highest = registers['nkr'] 
if 'nkr' not in registers.keys(): registers['nkr'] = 0 
if 'vh' not in registers.keys(): registers['vh'] = 0 
inc('nkr', 54) if registers['vh'] > -1982 else do_nothing()
if registers['nkr'] > highest:
   highest = registers['nkr'] 
if 'wfk' not in registers.keys(): registers['wfk'] = 0 
if 'g' not in registers.keys(): registers['g'] = 0 
inc('wfk', 109) if registers['g'] < -894 else do_nothing()
if registers['wfk'] > highest:
   highest = registers['wfk'] 
if 'afu' not in registers.keys(): registers['afu'] = 0 
if 'afu' not in registers.keys(): registers['afu'] = 0 
dec('afu', 439) if registers['afu'] <= 1553 else do_nothing()
if registers['afu'] > highest:
   highest = registers['afu'] 
if 'bfx' not in registers.keys(): registers['bfx'] = 0 
if 'ghj' not in registers.keys(): registers['ghj'] = 0 
inc('bfx', 471) if registers['ghj'] == -977 else do_nothing()
if registers['bfx'] > highest:
   highest = registers['bfx'] 
if 'nkr' not in registers.keys(): registers['nkr'] = 0 
if 'w' not in registers.keys(): registers['w'] = 0 
inc('nkr', 76) if registers['w'] >= 1027 else do_nothing()
if registers['nkr'] > highest:
   highest = registers['nkr'] 
if 'm' not in registers.keys(): registers['m'] = 0 
if 'yo' not in registers.keys(): registers['yo'] = 0 
inc('m', 420) if registers['yo'] <= -5160 else do_nothing()
if registers['m'] > highest:
   highest = registers['m'] 
if 'u' not in registers.keys(): registers['u'] = 0 
if 'a' not in registers.keys(): registers['a'] = 0 
dec('u', 379) if registers['a'] <= 79 else do_nothing()
if registers['u'] > highest:
   highest = registers['u'] 
if 'g' not in registers.keys(): registers['g'] = 0 
if 'lpi' not in registers.keys(): registers['lpi'] = 0 
dec('g', -318) if registers['lpi'] == -2182 else do_nothing()
if registers['g'] > highest:
   highest = registers['g'] 
if 'rlq' not in registers.keys(): registers['rlq'] = 0 
if 'g' not in registers.keys(): registers['g'] = 0 
dec('rlq', -827) if registers['g'] == -581 else do_nothing()
if registers['rlq'] > highest:
   highest = registers['rlq'] 
if 'vh' not in registers.keys(): registers['vh'] = 0 
if 'fkp' not in registers.keys(): registers['fkp'] = 0 
inc('vh', 985) if registers['fkp'] >= 1869 else do_nothing()
if registers['vh'] > highest:
   highest = registers['vh'] 
if 'afu' not in registers.keys(): registers['afu'] = 0 
if 'ghj' not in registers.keys(): registers['ghj'] = 0 
dec('afu', 451) if registers['ghj'] >= -979 else do_nothing()
if registers['afu'] > highest:
   highest = registers['afu'] 
if 'm' not in registers.keys(): registers['m'] = 0 
if 'qdq' not in registers.keys(): registers['qdq'] = 0 
dec('m', 366) if registers['qdq'] < -2678 else do_nothing()
if registers['m'] > highest:
   highest = registers['m'] 
if 'yo' not in registers.keys(): registers['yo'] = 0 
if 'yo' not in registers.keys(): registers['yo'] = 0 
dec('yo', -144) if registers['yo'] == -5160 else do_nothing()
if registers['yo'] > highest:
   highest = registers['yo'] 
if 't' not in registers.keys(): registers['t'] = 0 
if 'm' not in registers.keys(): registers['m'] = 0 
inc('t', -342) if registers['m'] > 3889 else do_nothing()
if registers['t'] > highest:
   highest = registers['t'] 
if 'k' not in registers.keys(): registers['k'] = 0 
if 'm' not in registers.keys(): registers['m'] = 0 
inc('k', 351) if registers['m'] <= 3900 else do_nothing()
if registers['k'] > highest:
   highest = registers['k'] 
if 'nkr' not in registers.keys(): registers['nkr'] = 0 
if 'rlq' not in registers.keys(): registers['rlq'] = 0 
inc('nkr', 232) if registers['rlq'] >= 1955 else do_nothing()
if registers['nkr'] > highest:
   highest = registers['nkr'] 
if 'afu' not in registers.keys(): registers['afu'] = 0 
if 'qn' not in registers.keys(): registers['qn'] = 0 
inc('afu', -56) if registers['qn'] != 4715 else do_nothing()
if registers['afu'] > highest:
   highest = registers['afu'] 
if 'qdq' not in registers.keys(): registers['qdq'] = 0 
if 'sh' not in registers.keys(): registers['sh'] = 0 
inc('qdq', 964) if registers['sh'] <= 959 else do_nothing()
if registers['qdq'] > highest:
   highest = registers['qdq'] 
if 'qn' not in registers.keys(): registers['qn'] = 0 
if 'pr' not in registers.keys(): registers['pr'] = 0 
inc('qn', -818) if registers['pr'] != -4520 else do_nothing()
if registers['qn'] > highest:
   highest = registers['qn'] 
if 'qrc' not in registers.keys(): registers['qrc'] = 0 
if 'afu' not in registers.keys(): registers['afu'] = 0 
inc('qrc', -291) if registers['afu'] > 592 else do_nothing()
if registers['qrc'] > highest:
   highest = registers['qrc'] 
if 't' not in registers.keys(): registers['t'] = 0 
if 'g' not in registers.keys(): registers['g'] = 0 
inc('t', 121) if registers['g'] < -577 else do_nothing()
if registers['t'] > highest:
   highest = registers['t'] 
if 'rlq' not in registers.keys(): registers['rlq'] = 0 
if 'u' not in registers.keys(): registers['u'] = 0 
inc('rlq', -364) if registers['u'] >= 1485 else do_nothing()
if registers['rlq'] > highest:
   highest = registers['rlq'] 
if 'u' not in registers.keys(): registers['u'] = 0 
if 'vh' not in registers.keys(): registers['vh'] = 0 
dec('u', -730) if registers['vh'] < -1002 else do_nothing()
if registers['u'] > highest:
   highest = registers['u'] 
if 'qrc' not in registers.keys(): registers['qrc'] = 0 
if 'rlq' not in registers.keys(): registers['rlq'] = 0 
dec('qrc', 612) if registers['rlq'] <= 1598 else do_nothing()
if registers['qrc'] > highest:
   highest = registers['qrc'] 
if 'g' not in registers.keys(): registers['g'] = 0 
if 't' not in registers.keys(): registers['t'] = 0 
inc('g', -540) if registers['t'] == -3678 else do_nothing()
if registers['g'] > highest:
   highest = registers['g'] 
if 'rlq' not in registers.keys(): registers['rlq'] = 0 
if 'wfk' not in registers.keys(): registers['wfk'] = 0 
dec('rlq', 717) if registers['wfk'] == -702 else do_nothing()
if registers['rlq'] > highest:
   highest = registers['rlq'] 
if 'wfk' not in registers.keys(): registers['wfk'] = 0 
if 'jh' not in registers.keys(): registers['jh'] = 0 
dec('wfk', 501) if registers['jh'] <= -2952 else do_nothing()
if registers['wfk'] > highest:
   highest = registers['wfk'] 
if 'qn' not in registers.keys(): registers['qn'] = 0 
if 'qdq' not in registers.keys(): registers['qdq'] = 0 
dec('qn', 502) if registers['qdq'] >= -1712 else do_nothing()
if registers['qn'] > highest:
   highest = registers['qn'] 
if 'qdq' not in registers.keys(): registers['qdq'] = 0 
if 'm' not in registers.keys(): registers['m'] = 0 
dec('qdq', -30) if registers['m'] >= 3891 else do_nothing()
if registers['qdq'] > highest:
   highest = registers['qdq'] 
if 'qn' not in registers.keys(): registers['qn'] = 0 
if 'nkr' not in registers.keys(): registers['nkr'] = 0 
inc('qn', 962) if registers['nkr'] < -8246 else do_nothing()
if registers['qn'] > highest:
   highest = registers['qn'] 
if 'm' not in registers.keys(): registers['m'] = 0 
if 'jh' not in registers.keys(): registers['jh'] = 0 
inc('m', 270) if registers['jh'] > -2970 else do_nothing()
if registers['m'] > highest:
   highest = registers['m'] 
if 'wfk' not in registers.keys(): registers['wfk'] = 0 
if 'yo' not in registers.keys(): registers['yo'] = 0 
dec('wfk', 872) if registers['yo'] == -5024 else do_nothing()
if registers['wfk'] > highest:
   highest = registers['wfk'] 
if 'yo' not in registers.keys(): registers['yo'] = 0 
if 'lpi' not in registers.keys(): registers['lpi'] = 0 
dec('yo', 872) if registers['lpi'] <= -2181 else do_nothing()
if registers['yo'] > highest:
   highest = registers['yo'] 
if 'bfx' not in registers.keys(): registers['bfx'] = 0 
if 'jq' not in registers.keys(): registers['jq'] = 0 
inc('bfx', 552) if registers['jq'] >= 2812 else do_nothing()
if registers['bfx'] > highest:
   highest = registers['bfx'] 
if 'fkp' not in registers.keys(): registers['fkp'] = 0 
if 'vh' not in registers.keys(): registers['vh'] = 0 
inc('fkp', -443) if registers['vh'] > -998 else do_nothing()
if registers['fkp'] > highest:
   highest = registers['fkp'] 
if 'nkr' not in registers.keys(): registers['nkr'] = 0 
if 'vh' not in registers.keys(): registers['vh'] = 0 
inc('nkr', 571) if registers['vh'] >= -992 else do_nothing()
if registers['nkr'] > highest:
   highest = registers['nkr'] 
if 'vh' not in registers.keys(): registers['vh'] = 0 
if 'qdq' not in registers.keys(): registers['qdq'] = 0 
dec('vh', -465) if registers['qdq'] >= -1682 else do_nothing()
if registers['vh'] > highest:
   highest = registers['vh'] 
if 'u' not in registers.keys(): registers['u'] = 0 
if 'nkr' not in registers.keys(): registers['nkr'] = 0 
inc('u', 613) if registers['nkr'] < -8246 else do_nothing()
if registers['u'] > highest:
   highest = registers['u'] 
if 'nkr' not in registers.keys(): registers['nkr'] = 0 
if 'rlq' not in registers.keys(): registers['rlq'] = 0 
inc('nkr', 63) if registers['rlq'] < 880 else do_nothing()
if registers['nkr'] > highest:
   highest = registers['nkr'] 
if 'qn' not in registers.keys(): registers['qn'] = 0 
if 'sh' not in registers.keys(): registers['sh'] = 0 
inc('qn', -430) if registers['sh'] == 957 else do_nothing()
if registers['qn'] > highest:
   highest = registers['qn'] 
if 'qrc' not in registers.keys(): registers['qrc'] = 0 
if 'pr' not in registers.keys(): registers['pr'] = 0 
inc('qrc', -495) if registers['pr'] > -4530 else do_nothing()
if registers['qrc'] > highest:
   highest = registers['qrc'] 
if 'vh' not in registers.keys(): registers['vh'] = 0 
if 'w' not in registers.keys(): registers['w'] = 0 
inc('vh', 229) if registers['w'] == 1034 else do_nothing()
if registers['vh'] > highest:
   highest = registers['vh'] 
if 'bfx' not in registers.keys(): registers['bfx'] = 0 
if 'jq' not in registers.keys(): registers['jq'] = 0 
inc('bfx', 184) if registers['jq'] >= 2801 else do_nothing()
if registers['bfx'] > highest:
   highest = registers['bfx'] 
if 'jq' not in registers.keys(): registers['jq'] = 0 
if 'lpi' not in registers.keys(): registers['lpi'] = 0 
inc('jq', -41) if registers['lpi'] <= -2192 else do_nothing()
if registers['jq'] > highest:
   highest = registers['jq'] 
if 'afu' not in registers.keys(): registers['afu'] = 0 
if 'wfk' not in registers.keys(): registers['wfk'] = 0 
dec('afu', 990) if registers['wfk'] < -1202 else do_nothing()
if registers['afu'] > highest:
   highest = registers['afu'] 

print(max(registers.items(), key=lambda k: k[1]))
print(highest)