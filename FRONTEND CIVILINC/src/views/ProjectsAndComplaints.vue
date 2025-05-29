<template>
  <div class="page03-container10">
    <!-- Sidebar -->
    <div class="page03-container11">
      <div class="sidebar-header">
        <span class="page03-text10">&lt;/&gt; Civilinc</span>
        <div class="page03-container12">
          <img src="/Shivayogi-pic.jpg" alt="Profile" class="page03-image" />
        </div>
        <span class="page03-text11">Welcome back,</span>
        <span class="page03-text12">Dr.Shivayogi.B.Yali</span>
        <span class="user-role">Municipal Commissioner</span>
      </div>

      <nav class="sidebar-nav">
        <router-link to="/dashboard" class="page03-link1">
          <i class="fas fa-chart-line"></i>
          Dashboard
        </router-link>
        <router-link to="/projects-complaints" class="page03-link2">
          <i class="fas fa-tasks"></i>
          Projects & Complaints
        </router-link>
        <router-link to="/map-forum" class="page03-link3">
          <i class="fas fa-map-marked-alt"></i>
          Map & Forum
        </router-link>
        <router-link to="/data-reports" class="page03-link4">
          <i class="fas fa-database"></i>
          Data & Reports
        </router-link>
        <router-link to="/budget-allocation" class="page03-link-new">
          <i class="fas fa-chart-pie"></i>
          Budget Allocation
        </router-link>
        <router-link to="/" class="page03-link6" @click="handleLogout">
          <i class="fas fa-sign-out-alt"></i>
          Logout
        </router-link>
      </nav>
    </div>

    <!-- Main Content -->
    <div class="main-content">
      <!-- Tabs for Projects and Complaints -->
      <div class="tabs-container">
        <button
          :class="['tab-button', { active: activeTab === 'projects' }]"
          @click="activeTab = 'projects'"
        >
          <i class="fas fa-tasks"></i>
          Projects
        </button>
        <button
          :class="['tab-button', { active: activeTab === 'complaints' }]"
          @click="activeTab = 'complaints'"
        >
          <i class="fas fa-clipboard-list"></i>
          Complaints
        </button>
      </div>

      <!-- Projects Tab Content -->
      <div v-if="activeTab === 'projects'" class="tab-content">
        <div class="section-header">
          <h2>Projects</h2>
          <button class="add-button" @click="handleAddProject">
            <i class="fas fa-plus"></i>
            Add Project
          </button>
        </div>
        <div class="filters">
          <input
            type="text"
            v-model="projectSearch"
            placeholder="Search projects..."
            class="search-input"
          />
          <select v-model="selectedProjectDepartment" class="filter-select">
            <option value="">All Departments</option>
            <option>Roads & Infrastructure</option>
            <option>Water Supply</option>
            <option>Waste Management</option>
            <option>Public Health</option>
            <option>Urban Planning</option>
          </select>
          <select v-model="selectedProjectStatus" class="filter-select">
            <option value="">All Statuses</option>
            <option>planned</option>
            <option>in-progress</option>
            <option>completed</option>
            <option>on-hold</option>
          </select>
        </div>

        <div v-if="loading" class="loading">Loading projects...</div>
        <div v-else-if="error" class="error">{{ error }}</div>
        <div v-else-if="filteredProjects.length === 0" class="empty-state">
          <i class="fas fa-box-open"></i>
          <p>No projects found.</p>
        </div>
        <div v-else class="table-responsive">
          <table class="data-table">
            <thead>
              <tr>
                <th>Title</th>
                <th>Department</th>
                <th>Status</th>
                <th>Budget</th>
                <th>Start Date</th>
                <th>End Date</th>
                <th>Actions</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="project in filteredProjects" :key="project.id">
                <td>{{ project.title }}</td>
                <td>{{ project.department }}</td>
                <td>
                  <span :class="['status-badge', project.status]">
                    {{ project.status }}
                  </span>
                </td>
                <td>₹{{ project.budget.toLocaleString() }}</td>
                <td>{{ project.start_date }}</td>
                <td>{{ project.end_date }}</td>
                <td>
                  <button class="action-icon" @click="handleViewProject(project)" title="View Project">
                    <i class="fas fa-eye"></i>
                  </button>
                  <button class="action-icon" @click="handleEditProject(project)" title="Edit Project">
                    <i class="fas fa-edit"></i>
                  </button>
                  <button class="action-icon delete-button" @click="handleDeleteProject(project.id)" title="Delete Project">
                    <i class="fas fa-trash"></i>
                  </button>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>

      <!-- Complaints Tab Content -->
      <div v-if="activeTab === 'complaints'" class="tab-content">
        <div class="section-header">
          <h2>Complaints</h2>
          <!-- Add Complaint button if needed -->
        </div>
        <div class="filters">
          <input
            type="text"
            v-model="complaintSearch"
            placeholder="Search complaints..."
            class="search-input"
          />
          <select v-model="selectedComplaintDepartment" class="filter-select">
            <option value="">All Departments</option>
            <option>Roads & Infrastructure</option>
            <option>Water Supply</option>
            <option>Waste Management</option>
            <option>Public Health</option>
            <option>Urban Planning</option>
          </select>
          <select v-model="selectedComplaintStatus" class="filter-select">
            <option value="">All Statuses</option>
            <option>pending</option>
            <option>in-progress</option>
            <option>resolved</option>
          </select>
        </div>

        <div v-if="loadingComplaints" class="loading">Loading complaints...</div>
        <div v-else-if="errorComplaints" class="error">{{ errorComplaints }}</div>
        <div v-else-if="filteredComplaints.length === 0" class="empty-state">
          <i class="fas fa-box-open"></i>
          <p>No complaints found.</p>
        </div>
        <div v-else class="table-responsive">
          <table class="data-table">
            <thead>
              <tr>
                <th>Title</th>
                <th>Department</th>
                <th>Status</th>
                <th>Date</th>
                <th>Category</th>
                <th>Assigned Officer</th>
                <th>Actions</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="complaint in filteredComplaints" :key="complaint.id">
                <td>{{ complaint.title }}</td>
                <td>{{ complaint.department }}</td>
                <td>
                  <span :class="['status-badge', complaint.status]">
                    {{ complaint.status }}
                  </span>
                </td>
                <td>{{ complaint.date }}</td>
                <td>{{ complaint.category }}</td>
                <td>{{ complaint.assigned_officer || 'Unassigned' }}</td>
                <td>
                   <button class="action-icon" @click="handleViewComplaint(complaint)" title="View Complaint">
                    <i class="fas fa-eye"></i>
                  </button>
                  <button class="action-icon" @click="handleEditComplaint(complaint)" title="Edit Complaint">
                    <i class="fas fa-edit"></i>
                  </button>
                   <button class="action-icon assign-button" @click="handleAssignOfficer(complaint)" title="Assign Officer">
                    <i class="fas fa-user-plus"></i>
                  </button>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>

      <!-- Modals -->
      <ProjectModal
        v-if="showProjectModal"
        :show-modal.sync="showProjectModal"
        :project="selectedProject"
        @save="handleSaveProject"
        @close="showProjectModal = false"
      />

      <ComplaintModal
        v-if="showComplaintModal"
        :show-modal.sync="showComplaintModal"
        :complaint="selectedComplaint"
        @save="handleSaveComplaint"
        @close="showComplaintModal = false"
      />

      <AssignOfficerModal
        v-if="showAssignOfficerModal"
        :show-modal.sync="showAssignOfficerModal"
        :complaint="selectedComplaint"
        @assign="handleAssignOfficerToComplaint"
        @close="showAssignOfficerModal = false"
      />
    </div>
  </div>
</template>

<script>
import { mapState, mapActions, mapGetters } from 'vuex';
import ProjectModal from '@/components/ProjectModal.vue';
import ComplaintModal from '@/components/ComplaintModal.vue';
import AssignOfficerModal from '@/components/AssignOfficerModal.vue';

export default {
  name: 'ProjectsAndComplaints',
  components: {
    ProjectModal,
    ComplaintModal,
    AssignOfficerModal
  },
  data() {
    return {
      activeTab: 'projects',
      projectSearch: '',
      complaintSearch: '',
      selectedProjectDepartment: '',
      selectedProjectStatus: '',
      selectedComplaintDepartment: '',
      selectedComplaintStatus: '',
      showProjectModal: false,
      showComplaintModal: false,
      showAssignOfficerModal: false,
      selectedProject: null,
      selectedComplaint: null,
      isMobile: false,
    };
  },
  computed: {
    ...mapState('projects', ['projects', 'loading', 'error']),
    ...mapState('complaints', {
      complaints: 'complaints',
      loadingComplaints: 'loading',
      errorComplaints: 'error'
    }),
    ...mapGetters('projects', ['filteredProjects:getFilteredProjects']),
    ...mapGetters('complaints', {
      filteredComplaints: 'getFilteredComplaints'
    })
  },
  methods: {
    ...mapActions('projects', [
      'fetchProjects',
      'fetchProjectById',
      'createProject',
      'updateProject',
      'deleteProject',
    ]),
    ...mapActions('complaints', [
      'fetchComplaints',
      'updateComplaintStatus',
      'assignOfficerToComplaint',
    ]),
    handleLogout() {
      // Implement logout logic if needed
      console.log('Logout');
    },
    handleAddProject() {
      this.selectedProject = null;
      this.showProjectModal = true;
    },
    handleViewProject(project) {
      this.selectedProject = project;
      this.showProjectModal = true;
    },
    handleEditProject(project) {
      this.selectedProject = project;
      this.showProjectModal = true;
    },
    async handleSaveProject(projectData) {
      try {
        if (projectData.id) {
          await this.updateProject(projectData);
          console.log('Project updated successfully');
        } else {
          await this.createProject(projectData);
          console.log('Project created successfully');
        }
        this.showProjectModal = false;
        this.fetchProjects(); // Refresh projects list
      } catch (error) {
        console.error('Error saving project:', error);
        // Show error message to user
      }
    },
    async handleDeleteProject(projectId) {
      if (confirm('Are you sure you want to delete this project?')) {
        try {
          await this.deleteProject(projectId);
          console.log('Project deleted successfully');
          this.fetchProjects(); // Refresh projects list
        } catch (error) {
          console.error('Error deleting project:', error);
          // Show error message to user
        }
      }
    },
    handleViewComplaint(complaint) {
      this.selectedComplaint = complaint;
      this.showComplaintModal = true;
    },
    handleEditComplaint(complaint) {
      this.selectedComplaint = complaint; // Reusing ComplaintModal for editing
      this.showComplaintModal = true;
    },
    handleAssignOfficer(complaint) {
       this.selectedComplaint = complaint;
       this.showAssignOfficerModal = true;
    },
    async handleAssignOfficerToComplaint(assignmentData) {
        try {
            await this.assignOfficerToComplaint(assignmentData);
            console.log('Officer assigned successfully');
            this.showAssignOfficerModal = false;
            this.fetchComplaints(); // Refresh complaints list
        } catch (error) {
            console.error('Error assigning officer:', error);
            // Show error message to user
        }
    },
    async handleSaveComplaint(complaintData) {
         try {
            // Assuming save means updating status or other fields via the Complaints module
            // The complaints module currently only has updateComplaintStatus and assignOfficerToComplaint
            // If 'save' from modal includes status updates, you'd call updateComplaintStatus
            // If it includes assigning officers, you'd call assignOfficerToComplaint
            // For now, let's assume it might involve status updates:
            if(complaintData && complaintData.id && complaintData.status) {
                 await this.updateComplaintStatus({ id: complaintData.id, status: complaintData.status });
                 console.log('Complaint updated successfully');
                 this.showComplaintModal = false;
                 this.fetchComplaints(); // Refresh complaints list
            } else {
                 console.warn('Save operation for complaint called without necessary data.');
                 // Handle cases where the modal save might be used for other purposes or is incomplete
                 this.showComplaintModal = false;
            }
        } catch (error) {
            console.error('Error saving complaint:', error);
            // Show error message to user
        }
    },
     handleResize() {
      this.isMobile = window.innerWidth <= 768;
    },
  },
   created() {
    this.fetchProjects();
    this.fetchComplaints();
     if (typeof window !== 'undefined') {
      window.addEventListener('resize', this.handleResize);
      this.handleResize(); // Set initial state
    }
  },
  beforeDestroy() {
    if (typeof window !== 'undefined') {
      window.removeEventListener('resize', this.handleResize);
    }
  },
  watch: {
    activeTab(newVal) {
      // Fetch data when tab changes if needed
      if (newVal === 'projects' && this.projects.length === 0) {
        this.fetchProjects();
      } else if (newVal === 'complaints' && this.complaints.length === 0) {
        this.fetchComplaints();
      }
    },
     // Watch for changes in route query for tab switching
    '$route.query.tab': {
      immediate: true,
      handler(newTab) {
        if (newTab) {
          this.activeTab = newTab;
        }
      }
    }
  }
};
</script>

<style scoped>
.page03-container10 {
  display: flex;
  min-height: 100vh;
  background-color: #f3f4f6; /* Use the background color from DataReportsPage */
}

.page03-container11 {
  width: 280px; /* Use the width from DataReportsPage */
  background-color: #1e40af; /* Use the background color from DataReportsPage */
  color: white; /* Use the text color from DataReportsPage */
  padding: 1.5rem; /* Use the padding from DataReportsPage */
  display: flex;
  flex-direction: column;
  /* Remove box-shadow and border-right for a cleaner look */
  /* box-shadow: 0 0 30px rgba(0, 0, 0, 0.1); */
  /* border-right: 2px solid rgba(37, 99, 235, 0.2); */
  position: fixed; /* Keep fixed positioning */
  left: 0;
  top: 0;
  bottom: 0; /* Extend to bottom */
  z-index: 100; /* Ensure it's on top */
  overflow-y: auto; /* Add scrolling for content overflow */
}

.sidebar-header {
  text-align: center; /* Center text */
  margin-bottom: 2rem; /* Space below header */
}

.page03-text10 {
  font-size: 1.5rem; /* Use font size from DataReportsPage */
  font-weight: bold; /* Use bold font weight from DataReportsPage */
  margin-bottom: 1rem; /* Use margin from DataReportsPage */
  display: block; /* Ensure it's a block element */
  color: white; /* Explicitly set color to white */
}

.page03-container12 {
  width: 80px; /* Use width from DataReportsPage */
  height: 80px; /* Use height from DataReportsPage */
  border-radius: 50%; /* Make it round */
  margin: 1rem auto; /* Center and add margin from DataReportsPage */
  border: 3px solid white; /* White border from DataReportsPage */
  overflow: hidden; /* Hide overflow for round image */
}

.page03-image {
  width: 100%; /* Image fills the container */
  height: 100%; /* Image fills the container */
  object-fit: cover; /* Crop image to cover the area */
}

.page03-text11,
.page03-text12 {
  display: block; /* Ensure block display from DataReportsPage */
  margin-bottom: 0.5rem; /* Use margin from DataReportsPage */
  color: white; /* Explicitly set color to white */
}

.user-role {
  font-size: 0.9rem; /* Use font size from DataReportsPage */
  opacity: 0.8; /* Use opacity from DataReportsPage */
  color: white; /* Explicitly set color to white */
}

.sidebar-nav {
  display: flex;
  flex-direction: column;
  gap: 0.5rem; /* Use gap from DataReportsPage */
}

.sidebar-nav a {
  color: white; /* Use white color for links from DataReportsPage */
  text-decoration: none; /* Remove underline */
  padding: 0.75rem 1rem; /* Use padding from DataReportsPage */
  border-radius: 0.5rem; /* Use border-radius from DataReportsPage */
  display: flex;
  align-items: center;
  gap: 0.75rem; /* Use gap from DataReportsPage */
  transition: background-color 0.3s; /* Use transition from DataReportsPage */
}

.sidebar-nav a:hover,
.sidebar-nav a.router-link-active {
  background-color: rgba(255, 255, 255, 0.1); /* Use hover/active background from DataReportsPage */
}

.sidebar-nav i {
  width: 20px; /* Use icon width from DataReportsPage */
  text-align: center;
  font-size: 1rem; /* Use icon font size from DataReportsPage */
}

.main-content {
  flex: 1; /* Allow main content to take remaining width */
  margin-left: 280px; /* Add left margin equal to sidebar width */
  padding: 2rem;
  overflow-y: auto; /* Add scrolling for content overflow */
}

/* Responsive Design */
@media (max-width: 768px) {
  .page03-container11 {
    position: relative; /* Change to relative on small screens */
    width: 100%;
    height: auto;
    z-index: auto;
    margin-left: 0;
    border-right: none;
    box-shadow: none;
    flex-direction: row;
    justify-content: space-around;
    padding: 1rem;
    align-items: center;
    background-color: #1e40af; /* Ensure consistent background on small screens */
    color: white; /* Ensure consistent text color on small screens */
  }

  .sidebar-header {
    display: none; /* Hide header on small screens */
  }

  .sidebar-nav {
    flex-direction: row;
    gap: 1rem;
    margin-top: 0;
    width: auto;
    flex-grow: 0;
  }

  .sidebar-nav a {
    padding: 0.5rem 0.8rem; /* Adjust padding */
    font-size: 0.8rem; /* Adjust font size */
    gap: 0.5rem; /* Adjust gap */
    flex-direction: column; /* Stack icon and text vertically */
    align-items: center; /* Center icon and text */
    color: white; /* Ensure consistent text color on small screens */
  }

  .sidebar-nav i {
    width: auto; /* Auto width for icons in stacked layout */
    font-size: 1rem; /* Adjust icon font size */
  }

  .page03-link6 {
    margin-top: 0;
  }

  .main-content {
    margin-left: 0;
    width: 100%;
    padding: 1rem;
  }
}

/* Styles for Tabs */
.tabs-container {
  display: flex;
  gap: 1rem;
  margin-bottom: 2rem;
  border-bottom: 2px solid #e5e7eb;
}

.tab-button {
  padding: 0.75rem 1.5rem;
  border: none;
  background-color: #e5e7eb;
  color: #4b5563;
  border-top-left-radius: 0.5rem;
  border-top-right-radius: 0.5rem;
  cursor: pointer;
  display: flex;
  align-items: center;
  gap: 0.5rem;
  transition: all 0.3s;
}

.tab-button:hover {
  background-color: #d1d5db;
}

.tab-button.active {
  background-color: white;
  color: #1e40af;
  border-bottom: 2px solid #1e40af;
}

.tab-content {
  background-color: white;
  border-radius: 0.5rem;
  padding: 2rem;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
}

/* Styles for Section Header */
.section-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 1.5rem;
}

.section-header h2 {
  font-size: 1.5rem;
  color: #1e40af;
}

.add-button {
  background-color: #1e40af;
  color: white;
  padding: 0.75rem 1.5rem;
  border: none;
  border-radius: 0.5rem;
  cursor: pointer;
  display: flex;
  align-items: center;
  gap: 0.5rem;
  transition: background-color 0.3s;
}

.add-button:hover {
  background-color: #1e3a8a;
}

/* Styles for Filters */
.filters {
  display: flex;
  gap: 1rem;
  margin-bottom: 1.5rem;
  flex-wrap: wrap;
}

.search-input,
.filter-select {
  padding: 0.5rem;
  border: 1px solid #d1d5db;
  border-radius: 0.375rem;
  font-size: 1rem;
}

/* Styles for Tables */
.table-responsive {
  overflow-x: auto;
}

.data-table {
  width: 100%;
  border-collapse: collapse;
  margin-top: 1rem;
}

.data-table th,
.data-table td {
  padding: 1rem;
  text-align: left;
  border-bottom: 1px solid #e5e7eb;
}

.data-table th {
  background-color: #f9fafb;
  font-weight: 600;
  color: #4b5563;
}

.data-table tbody tr:last-child td {
  border-bottom: none;
}

.status-badge {
  padding: 0.3rem 0.6rem;
  border-radius: 0.25rem;
  font-size: 0.8rem;
  font-weight: 600;
}

.status-badge.planned {
  background-color: #bfdbfe;
  color: #1e40af;
}

.status-badge.in-progress {
  background-color: #fde68a;
  color: #b45309;
}

.status-badge.completed {
  background-color: #d1fae5;
  color: #065f46;
}

.status-badge.on-hold {
  background-color: #fee2e2;
  color: #991b1b;
}

.status-badge.pending {
   background-color: #fef3c7; /* Light yellow */
   color: #92400e; /* Darker yellow */
}

.status-badge.resolved {
   background-color: #d1fae5; /* Light green */
   color: #065f46; /* Darker green */
}

/* Styles for Action Icons */
.action-icon,
.delete-button,
.assign-button {
  background: none;
  border: none;
  cursor: pointer;
  font-size: 1.1rem;
  margin-right: 0.8rem;
  transition: color 0.2s ease;
}

.action-icon:hover {
  color: #1e40af;
}

.delete-button {
  color: #ef4444; /* Red color for delete */
}

.delete-button:hover {
  color: #dc2626;
}

.assign-button {
   color: #22c55e; /* Green color for assign */
}

.assign-button:hover {
   color: #16a34a; /* Darker green */
}

/* Styles for Modals */
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000;
}

.modal-content {
  background-color: white;
  padding: 2rem;
  border-radius: 0.5rem;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.2);
  max-width: 600px;
  width: 90%;
  max-height: 90%;
  overflow-y: auto;
}

.modal-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 1.5rem;
  border-bottom: 1px solid #e5e7eb;
  padding-bottom: 1rem;
}

.modal-header h3 {
  margin: 0;
  font-size: 1.5rem;
  color: #1e40af;
}

.close-button {
  background: none;
  border: none;
  font-size: 1.5rem;
  cursor: pointer;
  color: #6b7280;
}

.close-button:hover {
  color: #374151;
}

.modal-body {
  margin-bottom: 1.5rem;
}

/* Styles for empty state */
.empty-state {
  text-align: center;
  padding: 2rem;
  color: #6b7280;
}

.empty-state i {
  font-size: 3rem;
  margin-bottom: 1rem;
}

.empty-state p {
  font-size: 1.2rem;
}

/* Styles for loading/error */
.loading,
.error {
  text-align: center;
  padding: 1rem;
  font-size: 1.2rem;
}

.error {
  color: #ef4444;
}

/* Responsive adjustments for ProjectsAndComplaints */
@media (max-width: 768px) {
  .data-table th,
  .data-table td {
    padding: 0.8rem;
  }
  
  .filters {
    flex-direction: column;
    gap: 0.8rem;
  }
  
  .search-input,
  .filter-select {
    width: 100%;
    box-sizing: border-box;
  }
}
</style> 