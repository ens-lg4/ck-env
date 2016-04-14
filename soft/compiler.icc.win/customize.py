#
# Collective Knowledge (individual environment - setup)
#
# See CK LICENSE.txt for licensing details
# See CK COPYRIGHT.txt for copyright details
#
# Developer: Grigori Fursin, Grigori.Fursin@cTuning.org, http://fursin.net
#

##############################################################################
# setup environment setup

def setup(i):
    """
    Input:  {
              cfg              - meta of this soft entry
              self_cfg         - meta of module soft
              ck_kernel        - import CK kernel module (to reuse functions)

              host_os_uoa      - host OS UOA
              host_os_uid      - host OS UID
              host_os_dict     - host OS meta
              
              target_os_uoa    - target OS UOA
              target_os_uid    - target OS UID
              target_os_dict   - target OS meta

              target_device_id - target device ID (if via ADB)

              tags             - list of tags used to search this entry

              env              - updated environment vars from meta
              customize        - updated customize vars from meta

              deps             - resolved dependencies for this soft

              interactive      - if 'yes', can ask questions, otherwise quiet
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0

              bat          - prepared string for bat file
            }

    """

    import os

    # Get variables
    ck=i['ck_kernel']
    s=''

    iv=i.get('interactive','')

    env=i.get('env',{})
    cfg=i.get('cfg',{})
    deps=i.get('deps',{})
    tags=i.get('tags',[])
    cus=i.get('customize',{})

    host_d=i.get('host_os_dict',{})
    target_d=i.get('target_os_dict',{})
    winh=host_d.get('windows_base','')
    win=target_d.get('windows_base','')
    mingw=target_d.get('mingw','')
    tbits=target_d.get('bits','')

    envp=cus.get('env_prefix','')
    pi=cus.get('path_install','')

    ################################################################
    # Check which version of visual studio is used
    vs=''

    vsx=deps['compiler_mcl']
    ver=vsx.get('ver','')

    if ver.startswith('15.'): vs='vs2008shell'
    elif ver.startswith('18.'): vs='vs2013'
    else:
       if iv=='yes':
          ra=ck.inp({'text':'Enter Visual Studio dependency (vs2008shell or vs2013): '})
          vs=ra['string'].strip()
       else:
          return {'return':1, 'error':'Visual Studio version is not recognized - should be either 15.x or 18.x'}

    s+='\n'
    s+='rem Setting Intel compiler environment\n'

    yy='call "'+pi+'\\bin\\compilervars.bat" '

    if tbits=='32': yy+=' ia32'
    else: yy+=' intel64'

    s+=yy+' '+vs+'\n\n'

    return {'return':0, 'bat':s}
