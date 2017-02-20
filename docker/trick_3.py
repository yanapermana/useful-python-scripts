from cgroups import Cgroup
from cgroups.user import create_user_cgroups
import os
import subprocess

try:
    # setup cgroup directory for this user
    user = os.getlogin()
    create_user_cgroups(user)

    # First we create the cgroup and we set it's cpu and memory limits
    cg = Cgroup(name)
    cg.set_cpu_limit(50)  # TODO : get these as command line options
    cg.set_memory_limit(500)

    # Then we a create a function to add a process in the cgroup
    def in_cgroup():
        try:
            pid = os.getpid()
            cg = Cgroup(name)
            for env in env_vars:
                log.info('Setting ENV %s' % env)
                os.putenv(*env.split('=', 1))

            # add process to cgroup
            cg.add(pid)

            os.chroot(layer_dir)
            if working_dir != '':
                log.info("Setting working directory to %s" % working_dir)
                os.chdir(working_dir)
        except Exception as e:
            traceback.print_exc()
            log.error("Failed to preexecute function")
            log.error(e)
    cmd = start_cmd
    log.info('Running "%s"' % cmd)
    process = subprocess.Popen(cmd, preexec_fn=in_cgroup, shell=True)
    process.wait()
    print(process.stdout)
log.error(process.stderr)
